from datetime import datetime
from django.db import models


# Create your models here.

class DNS(models.Model):
    DNS_TYPE_CHOICES = [
        ('A', 'A记录'),
        ('AAAA', 'AAAA记录'),
        ('CNAME', 'CNAME记录'),
        ('MX', 'MX记录'),
        ('TXT', 'TXT记录'),
        ('NS', 'NS记录'),
        ('PTR', 'PTR记录'),
        ('SRV', 'SRV记录'),
    ]

    STATUS_CHOICES = [
        (1, '可用'),
        (0, '不可用'),
    ]

    name = models.CharField(max_length=32, blank=False, verbose_name='站点名称')
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='目标IP地址')
    record_type = models.CharField(max_length=10, choices=DNS_TYPE_CHOICES, default='A', verbose_name='记录类型')
    ttl = models.IntegerField(default=3600, verbose_name='TTL值')
    dns_server = models.CharField(max_length=128, blank=True, verbose_name='DNS服务器')
    priority = models.IntegerField(default=10, verbose_name='优先级')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='状态')
    description = models.TextField(blank=True, verbose_name='备注说明')
    created_time = models.DateTimeField(verbose_name='记录时间', default=datetime.now)
    updated_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)

    class Meta:
        verbose_name = 'dns'
        verbose_name_plural = verbose_name
        ordering = ['priority', '-created_time']

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<%s>' % self.name

