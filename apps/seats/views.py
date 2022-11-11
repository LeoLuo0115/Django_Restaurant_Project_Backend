from django.shortcuts import render
from apps.user.models import Account
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.db import connection
import json
from apps.seats.models import Desk, Booking


def reserve(request):
    print("预定post请求")

    print("request body", request.body)

    post_dict = json.loads(str(request.body, encoding="utf-8"))
    print("post_dict", post_dict)

    headcount = post_dict.get("headcount")
    startTime = post_dict.get("startTime")
    endTime = post_dict.get("endTime")
    datetime = post_dict.get("datetime")[:10] + " 00:00:00"
    name = post_dict.get("name")
    phone_number = post_dict.get("phonenumber")
    email = post_dict.get("email")
    value = post_dict.get("value")
    login_check = post_dict.get("login_check")
    print("date", datetime)
    print("s", startTime)
    print("e", endTime)

    """
    库里： st = 9：00  et = 12：00
    预定： st = 8：00  et = 11：00
    
    startTime, endTime 都是入参
    
    // 判断是重叠时间段
    start_time  < endTime 
    9：00 < 11:00
    
    stop_time > startTime
    12：00 > 8：00
    
    // 
    """

    # 判断是重叠时间段 / Determine if it is an overlapping time period
    try:
        booking_list = Booking.objects.filter(date_time=datetime, start_time__lt=endTime, stop_time__gt=startTime)
        print("booking_list = ", booking_list)
    except Exception as e:
        print("异常：", e)

    desk_nos = []  # 当前时间 已经被预定的桌子编号 / Current time, Number(id) of tables already booked
    for book_obj in booking_list:
        desk_no = book_obj.desk_no
        print("desk_no = ", desk_no)

        # 添加已经被预定的桌子编号到数组  方法一
        # desk_nos.extend(int(no) for no in (book_obj.desk_no.split(",")))
        # 方法二
        desk_no_list = book_obj.desk_no.split(",")
        # print("desk_no_lis == ", desk_no_list)
        for desk_no in desk_no_list:
            desk_nos.append(int(desk_no))

    print("desk_nos = ", desk_nos)

    desk_objs = Desk.objects.exclude(desk_no__in=desk_nos)  # Exclude tables that are already booked
    desk_list = []
    # 查询可预订的桌子 / Check available tables
    for desk_obj in desk_objs:
        desk_list.append({
            "desk_no": desk_obj.desk_no,
            "desk_seat": desk_obj.desk_seat,
        })
    print("desk_list == ", desk_list)

    # 筛选符合 预定人数的桌子 / Filter the tables to match the number of people booked
    # 一张桌子，先不拼桌 / Find an available table, without putting together a table first
    desk_no_str = ''
    for desk in desk_list:
        if desk["desk_seat"] >= headcount:
            desk_no_str = desk["desk_no"]
            break
    print("desk id", desk_no_str)
    # 拼桌 / A single table is not enough, need to put together a table
    if not desk_no_str:
        try:
            desk_list_len = len(desk_list)
            for i in range(desk_list_len):  # 0，1，2
                for j in range(i + 1, desk_list_len):  # 1，2
                    desk_i = desk_list[i]
                    desk_j = desk_list[j]
                    if desk_i["desk_seat"] + desk_j["desk_seat"] >= headcount:
                        desk_no_str = str(desk_i["desk_no"]) + "," + str(desk_j["desk_no"])
                        break
                if desk_no_str:
                    break
        except Exception as e:
            print("异常：", e)
    print("desk_no_str = ", desk_no_str)

    if desk_no_str:
        # 查用户id
        if login_check:
            user = User.objects.filter(username=login_check)
            user_id = user[0].id
        else:
            user_id = -1

        print("user_id == ", user_id)
        # 记录到 预定表
        try:
            booking = Booking(date_time=datetime, start_time=startTime, stop_time=endTime,
                              preferred_payment_method=value,
                              people_number=headcount, desk_no=desk_no_str, status=1, name=name, user=user_id,
                              phone_number=phone_number, email_address=email)
            booking.save()
        except Exception as e:
            result = {
                "code": "988",
                "msg": "预定异常！！！",
                "data": [
                    {
                        "desk_number": desk_no_str,
                        "value": value
                    }
                ]
            }
            print(result)
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")
        else:
            try:
                # 更新用户默认的支付方式
                user_obj = Account.objects.filter(name=login_check)
                print("user_obj = ", user_obj)
                user_obj.update(preferred_payment_method=value)
            except Exception as e:
                print("异常：", e)

        result = {
            "code": "200",
            "msg": "预定成功 / reserved successfully！！！",
            "data": [
                {
                    "desk_number": desk_no_str,
                    "value": value
                }
            ]
        }
        print(result)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")
    else:
        result = {
            "code": "999",
            "msg": "预定失败 / reserved failed！！！",
            "data": [
                {
                    "desk_number": desk_no_str,
                    "value": value
                }
            ]
        }
        print(result)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")
