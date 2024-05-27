from datetime import datetime
from django.db import models

# Create your models here.
class Burp(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='名称')
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='IP地址')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)

    class Meta:
        verbose_name = 'burp'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Burp %s>' % self.name


class BurpResult(models.Model):
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='目标ip地址')
    port = models.CharField(max_length=128, blank=False, verbose_name='端口')
    account = models.CharField(max_length=128, blank=False, verbose_name='账号')
    password = models.CharField(max_length=128, blank=False, verbose_name='密码')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)

    class Meta:
        verbose_name = 'burp_result'

    def __str__(self):
        return self.ipaddr

    def __repr__(self):
        return '<BurpResult %s>' % self.ipaddr
