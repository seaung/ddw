from datetime import datetime
from django.db import models

# Create your models here.
class Burp(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='名称')
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='IP地址')

    class Meta:
        verbose_name = 'burp'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Burp %s>' % self.name

