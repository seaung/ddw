from celery import shared_task
from datetime import datetime
from .models import DNS
import dns.resolver


@shared_task
def dns_check_task(dns_id: int):
    """即时执行的DNS解析任务"""
    try:
        dns_record = DNS.objects.get(id=dns_id)
        resolver = dns.resolver.Resolver()
        
        if dns_record.dns_server:
            resolver.nameservers = [dns_record.dns_server]
        
        # 执行DNS解析
        answers = resolver.resolve(dns_record.name, dns_record.record_type)
        
        # 验证解析结果
        resolved_ips = [str(rdata) for rdata in answers]
        if dns_record.ipaddr in resolved_ips:
            dns_record.status = 1
        else:
            dns_record.status = 0
        
        dns_record.updated_time = datetime.now()
        dns_record.save()
        return True
    except Exception as e:
        if dns_record:
            dns_record.status = 0
            dns_record.save()
        return False


@shared_task
def scheduled_dns_check(dns_id: int):
    """定时执行的DNS检查任务"""
    return dns_check_task(dns_id)


@shared_task
def periodic_dns_check():
    """周期性执行的DNS检查任务"""
    try:
        # 获取所有可用的DNS记录
        dns_records = DNS.objects.filter(status=1)
        for dns_record in dns_records:
            dns_check_task(dns_record.id)
        return True
    except Exception as e:
        return False