from django.shortcuts import render
from apps.user.models import Account
from django.http import HttpResponse, JsonResponse
import json

from django.contrib.auth.models import User


# Create your views here.
def registered(request):
    if request.method == "POST":  # 表单 接口
        print("post请求")
        username = request.POST.get("username")
        password = request.POST.get("password")
        mailing_address = request.POST.get("mailing_address")
        billing_address = request.POST.get("billing_address")
        value = request.POST.get("value")  # 支付方式

        print("username = ", username)
        print("password = ", password)
        print("mailing_address = ", mailing_address)
        print("billing_address = ", billing_address)
        print("value = ", value)
        mailing_address = "kwjhdsf"
        billing_address = "7as8d9"
        value = 1

        if username and 6 <= len(username) <= 16:
            user_list = User.objects.filter(username=username)
            print("user_list = ", user_list)
            if user_list:
                result = {
                    "code": 0000,
                    "msg": "该账号已存在,this！！！"
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
                                           billing_address=billing_address, preferred_payment_method=value)
                    user_account.save()
                    # return render(request, "register_auth.html", {"year": "2022", "month": "10", "day": "17"})
                    result = {
                        "code": 600,
                        "msg": "注册成功！！！",
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
                        "code": 9999,
                        "msg": "参数输入不正确！！！"
                    }
                    # return JsonResponse(result)
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json; charset=utf-8")


        else:
            result = {
                "code": 9999,
                "msg": "username输入不正确！！！"
            }
            # return JsonResponse(result)
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json; charset=utf-8")

    else:
        print("get请求")
        return render(request, "register_auth.html", {"year": "2022", "month": "10", "day": "17"})
