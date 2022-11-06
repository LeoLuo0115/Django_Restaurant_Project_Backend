from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PAYMENT_METHOD_CHOICES = (
    (1, 'cash'),
    (2, 'credit card'),
    (3, 'check')
)

DISHES = (
    (1, '白菜1'),
    (2, '白菜2'),
    (3, '白菜3'),
)


class Account(models.Model):
    name = models.CharField(max_length=30)  # 字段长度
    mailing_address = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    star_points = models.FloatField(max_length=200, default=0)  # Float类型字段要加 default
    #  首选支付方式使用整数类型来映射到全局变量 PAYMENT_METHOD_CHOICES, 如果什么都没穿需要加上 null=True, blank=True
    preferred_payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    #  user来连接到 Django 自带的 User list / on_delete 当User删除，account也会被删除因为是一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 首选菜品
    preferred_dish = models.IntegerField(null=False, blank=True)
