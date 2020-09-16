from django.db import models
from django.contrib.auth.models import AbstractUser# django自带的认证系统中，用户表的抽象接口
# 在django自带的用户表中扩展列

class UsersModel(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机', default='')
    age = models.CharField(max_length=5, default='', verbose_name='年龄')
    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
