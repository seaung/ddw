from datetime import datetime
from django.db import models


# Create your models here.
# Burp模型用于存储目标扫描任务的基本信息
class Burp(models.Model):
    # 扫描任务基本信息
    name = models.CharField(max_length=128, blank=False, verbose_name='任务名称')
    target_url = models.URLField(max_length=256, blank=False, verbose_name='目标URL')
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='IP地址')
    
    # 扫描配置
    SCAN_TYPE_CHOICES = [
        ('active', '主动扫描'),
        ('passive', '被动扫描'),
        ('mixed', '混合扫描')
    ]
    scan_type = models.CharField(max_length=10, choices=SCAN_TYPE_CHOICES, default='active', verbose_name='扫描类型')
    
    SCAN_STATUS_CHOICES = [
        ('pending', '等待扫描'),
        ('running', '扫描中'),
        ('completed', '已完成'),
        ('failed', '扫描失败')
    ]
    scan_status = models.CharField(max_length=10, choices=SCAN_STATUS_CHOICES, default='pending', verbose_name='扫描状态')
    
    RISK_LEVEL_CHOICES = [
        ('high', '高危'),
        ('medium', '中危'),
        ('low', '低危'),
        ('info', '信息')
    ]
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES, default='info', verbose_name='风险等级')
    
    description = models.TextField(blank=True, verbose_name='任务描述')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = 'burp'

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Burp %s>' % self.name


class BurpResult(models.Model):
    # 关联扫描任务
    burp = models.ForeignKey(Burp, on_delete=models.CASCADE, verbose_name='所属任务')
    
    # 漏洞基本信息
    ipaddr = models.CharField(max_length=128, blank=False, verbose_name='目标IP地址')
    port = models.CharField(max_length=128, blank=False, verbose_name='端口')
    
    # 漏洞详情
    VULN_TYPE_CHOICES = [
        ('sqli', 'SQL注入'),
        ('xss', 'XSS跨站'),
        ('rce', '远程命令执行'),
        ('file_upload', '文件上传'),
        ('info_leak', '信息泄露'),
        ('other', '其他')
    ]
    vuln_type = models.CharField(max_length=20, choices=VULN_TYPE_CHOICES, default='other', verbose_name='漏洞类型')
    vuln_description = models.TextField(blank=True, verbose_name='漏洞描述')
    poc = models.TextField(blank=True, verbose_name='验证POC')
    
    # 认证信息
    account = models.CharField(max_length=128, blank=True, verbose_name='账号')
    password = models.CharField(max_length=128, blank=True, verbose_name='密码')
    
    # 修复建议
    fix_suggestion = models.TextField(blank=True, verbose_name='修复建议')
    
    # 验证状态
    VERIFY_STATUS_CHOICES = [
        ('unverified', '未验证'),
        ('verified', '已验证'),
        ('false_positive', '误报')
    ]
    verify_status = models.CharField(max_length=15, choices=VERIFY_STATUS_CHOICES, default='unverified', verbose_name='验证状态')
    
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = 'burp_result'

    def __str__(self):
        return self.ipaddr

    def __repr__(self):
        return '<BurpResult %s>' % self.ipaddr
