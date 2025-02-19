import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'didiwei.settings')

app = Celery('didiwei')
app.config_from_object('django.conf:settings', namespace='CELERY')

# 配置定时任务
app.conf.beat_schedule = {
    'periodic-burp-scan': {
        'task': 'burp.tasks.periodic_burp_scan',
        'schedule': crontab(minute='0', hour='*/12'),  # 每12小时执行一次
        'args': (1,),  # 传入burp_id参数
    },
}

app.autodiscover_tasks()