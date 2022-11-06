# import datetime
#
# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator
# from django.utils.timezone import now
#
# # Create your models here.
#
#
# SEAT_NUMBER_CHOICES = (
#     (2, 'two seats'),
#     (4, 'four seats'),
#     (6, 'six seats'),
#     (8, 'eight seats')
# )
#
# PAYMENT_METHOD_CHOICES = (
#     (1, 'cash'),
#     (2, 'credit card'),
#     (3, 'check')
# )
#
#
# class Seat(models.Model):
#     number = models.IntegerField(choices=SEAT_NUMBER_CHOICES)
#
#     def is_available(self, time):
#         time_range = (time - datetime.timedelta(hours=1), time + datetime.timedelta(hours=1))
#         return self.booking_set.all().filter(datetime__range=time_range)
#
#
# class Booking(models.Model):
#     datetime = models.DateTimeField()
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     preferred_payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
#     # people_number = models.IntegerField(valid1ators=(MaxValueValidator(14)))
#     seats = models.ManyToManyField(Seat)  # 可以查这张桌子被哪些用户使用过
#
#
# """
# # 固定选择时间段 /
#
# time
# 9 10 11
#
# id
# 1 2 5 6
# numbers
# 2 4 6 8
#
# 7
#
# Booking
#     ...
#     seats
#         5,1
# """

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils.timezone import now

# Create your models here.


PAYMENT_METHOD_CHOICES = (
    (1, 'cash'),
    (2, 'credit card'),
    (3, 'check')
)


# 桌子表
class Desk(models.Model):
    desk_no = models.IntegerField(verbose_name="桌子编号")
    desk_seat = models.IntegerField(verbose_name="桌子座位数")  # 桌子座位数  2, 4, 6, 8
    desk_status = models.IntegerField(verbose_name="桌子状态")  # 1 可用，0 停用

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    remark = models.CharField(max_length=128, null=True, blank=True, default="", verbose_name="备注")


# 预定表
class Booking(models.Model):

    date_time = models.DateTimeField()
    start_time = models.TimeField()
    stop_time = models.TimeField()

    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.IntegerField(null=True, verbose_name="用户的id")
    preferred_payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    people_number = models.IntegerField(validators=(MaxValueValidator(14),), verbose_name="预定人数")
    desk_no = models.CharField(max_length=255, verbose_name="预定桌子的编号")
    status = models.IntegerField(default=1, verbose_name="预定状态")  # 1 预定，0 取消预订

    name = models.CharField(max_length=255, verbose_name="姓名")
    phone_number = models.CharField(max_length=255, verbose_name="手机号码")
    email_address = models.CharField(max_length=255, verbose_name="邮件号码")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    remark = models.CharField(max_length=128, null=True, blank=True, default="", verbose_name="备注")
