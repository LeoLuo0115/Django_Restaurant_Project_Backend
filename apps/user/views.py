import random

from django.shortcuts import render
from apps.user.models import Account
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.db import connection
import json

from django.contrib.auth.models import User


# Create your views here.
def registered(request):
    if request.method == "POST":  # 表单 接口
        print("注册post请求")

        print("request body", request.POST)

        post_dict = json.loads(str(request.body, encoding="utf-8"))
        username = post_dict.get("username")
        # username = post_dict["username"]
        password = post_dict.get("password")

        mailing_address = post_dict.get("mailing_address")
        billing_address = post_dict.get("billing_address")
        value = post_dict.get("value")  # 支付方式

        print("username = ", username)
        print("password = ", password)
        print("mailing_address = ", mailing_address)
        print("billing_address = ", billing_address)
        print("value = ", value)
        # mailing_address = "kwjhdsf"
        # billing_address = "7as8d9"
        # value = 1

        if username and 6 <= len(username) <= 14:
            user_list = User.objects.filter(username=username)
            print("user_list = ", user_list)
            if user_list:
                result = {
                    "code": "9999",
                    # "msg": "该账号已存在！！！",
                    "msg": "This account already exist！！！"
                }
                # return JsonResponse(result)
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json; charset=utf-8")

            else:
                # 校验参数
                if password and 6 <= len(password) <= 14 and (value in (1, 2, 3)):
                    user1 = User.objects.create_user(username=username, password=password, is_staff=1)
                    user1.save()
                    user_account = Account(user=user1, name=username, mailing_address=mailing_address,
                                           billing_address=billing_address, preferred_payment_method=value,
                                           preferred_dish=random.randint(1, 4))
                    user_account.save()
                    # return render(request, "register_auth.html", {"year": "2022", "month": "10", "day": "17"})
                    result = {
                        "code": "200",
                        # "msg": "注册成功！！！",
                        "msg": "Register Successfully!",
                        "data": [
                            {
                                "username": username
                            }
                        ]
                    }
                    # return JsonResponse(result)
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json; charset=utf-8")

                else:
                    result = {
                        "code": "9999",
                        "msg": "参数输入不正确！！！"
                    }
                    # return JsonResponse(result)
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json; charset=utf-8")


        else:
            result = {
                "code": "9999",
                "msg": "username输入不正确！！！"
            }
            # return JsonResponse(result)
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")

    else:
        print("get请求")
        return render(request, "register_auth.html", {"year": "2022", "month": "10", "day": "17"})


def login_post(request):
    """登录"""
    """
    登录：
    1：校验username和password的值
    2、调框架自己登录接口
    3、登录结果
    """
    if request.method == "POST":  # 表单 接口
        print("登录post请求")
        # username = request.POST.get("username")
        # password = request.POST.get("password", None)

        print("request body", request.POST)

        post_dict = json.loads(str(request.body, encoding="utf-8"))
        username = post_dict.get("username")
        # username = post_dict["username"]
        password = post_dict.get("password")

        print("username= ", username)
        print("password = ", password)

        if username and password:
            # django框架认证
            user = authenticate(username=username, password=password, is_active=1)
            print("user = ", user, type(user))
            if user:
                print("认证成功")
                # print("authenticate successfully")

                if user.is_active == 1:
                    # login(request, user=user)
                    print("登陆成功")
                    # print("login successfully")
                    result = {
                        "code": "200",
                        "msg": "登陆成功 / login successfully！！！",
                        "data": [
                            {
                                 # "value": value
                            }
                    ]
                    }
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json; charset=utf-8")

                else:
                    print("该账号已被冻结")
                    result = {
                        "code": "9999",
                        "msg": "该账号已被冻结！！！"
                    }
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json; charset=utf-8")

            else:
                print("username或者password不存在")
                result = {
                    "code": "9999",
                    # "msg": "username或者password不存在！！！"
                    "msg": "username or password does not exists！！！"
                }
                # return JsonResponse(result)
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json; charset=utf-8")

        else:
            print("username或者password不能为空")
            result = {
                "code": "9999",
                "msg": "username或者password不能为空！！！"
            }
            # return JsonResponse(result)
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")

    else:
        print("请用post请求")
        result = {
            "code": "9999",
            "msg": "请用post请求！！！"
        }
        # return JsonResponse(result)

        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")


def test(request):
    """学习数据库  orm 操作"""
    print("orm测试")
    """一、查询"""
    # raw 方法 执行sql
    # user_objects = User.objects.raw("select * from auth_user where id=6")
    # print("user_objects = ", user_objects, type(user_objects))  # RawQueryset
    # for user_object in user_objects:

    #     print("user_object = ", user_object, type(user_object))
    #     print("username = ", user_object.username)
    #     print("username  id = ", user_object.id)

    # 游标查询
    # cursor = connection.cursor()
    # cursor.execute("select * from auth_user")
    # # 返回一行数据
    # # user_object= cursor.fetchone()
    # # print("user_object= ", user_object, type(user_object))  # 元组类型  []
    #
    # # 返回多行数据
    # user_objects = cursor.fetchall()
    # print("user_objects = ", user_objects, type(user_objects))
    # for user_object in user_objects:
    #     print("username id = ", user_object[0], type(user_object))

    # filter 查询
    # user_objects = User.objects.filter()  # 不带条件  查询所有
    # user_objects = User.objects.filter(id=7, username="1234567")  # 带指定条件查询
    # user_objects = User.objects.filter(id__exact=7, username__exact="1234567")  # 带指定条件查询
    # user_objects = User.objects.filter(username__contains="34")  # 包含
    # user_objects = User.objects.filter(id__in=[6, 7])  # 包含
    # user_objects = User.objects.filter(id__gt=6)  # 大于
    # user_objects = User.objects.filter(id__lt=7)  # 小于
    # user_objects = User.objects.filter(username__istartswith="12")
    # user_objects = User.objects.filter(username__endswith="7")

    # user_objects = User.objects.filter().values("id", "username")  # values 查询的字段
    # user_objects = User.objects.filter().values_list("id", "username")  # values 查询的字段
    # print("user_objects = ", user_objects, type(user_objects))
    # for user_object in user_objects:
    #     print("username id = ", user_object, type(user_object))
    #     print("id = ", user_object.id)
    #     print("name = ", user_object.username)

    # all 方法
    # user_objects = User.objects.all().values("id", "username")
    # user_objects = User.objects.all().values_list("id", "username")
    # print("user_objects all = ", user_objects, type(user_objects))
    # for user_object in user_objects:
    #     print("username id = ", user_object, type(user_object))
    #     print("id = ", user_object.id)
    #     print("name = ", user_object.username)

    # get 方法
    # user_object = User.objects.get(id=7)
    # print("user_objects all = ", user_object, type(user_object))
    # print("id = ", user_object.id)
    # print("name = ", user_object.username)

    # get_or_create
    # user_object = User.objects.get_or_create(username="自动")
    # print("user_objects all = ", user_object, type(user_object))

    # or
    # user_objects = User.objects.filter(id__exact=7, username__exact="1234567")  # 带指定条件查询
    # user_objects = User.objects.filter(Q(id__exact=7), Q(username__exact="123456"))  # 带指定条件查询  and
    # user_objects = User.objects.filter(Q(id__exact=7) | Q(username__exact="123456"))  # 带指定条件查询  and
    # print("user_objects all = ", user_objects, type(user_objects))
    # for user_object in user_objects:
    #     print("username id = ", user_object, type(user_object))
    #     print("id = ", user_object.id)
    #     print("name = ", user_object.username)
