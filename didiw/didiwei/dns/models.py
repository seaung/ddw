from datetime import datetime
from django.db import models


# Create your models here.

class DNS(models.Model):
    name = models.CharField(max_length=32, blank=False, verbose_name='站点名称')
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='目标IP地址')
    created_time = models.DateTimeField(verbose_name='记录时间', default=datetime.now)
    updated_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)

    class Meta:
        verbose_name = 'dns'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<%s>' % self.name

