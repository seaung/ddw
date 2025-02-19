from django.contrib import admin
from django.utils.html import format_html
from .models import DNS
from .tasks import dns_check_task


@admin.register(DNS)
class DNSAdmin(admin.ModelAdmin):
    list_display = ['name', 'ipaddr', 'record_type', 'dns_server', 'priority', 'status_tag', 'created_time', 'updated_time']
    list_filter = ['status', 'record_type', 'priority']
    search_fields = ['name', 'ipaddr', 'dns_server', 'description']
    ordering = ['priority', '-created_time']
    
    def status_tag(self, obj):
        if obj.status == 1:
            return format_html('<span style="color: green;">可用</span>')
        return format_html('<span style="color: red;">不可用</span>')
    status_tag.short_description = '状态'
    
    actions = ['check_dns_now']
    
    def check_dns_now(self, request, queryset):
        for dns in queryset:
            dns_check_task.delay(dns.id)
        self.message_user(request, f'已触发 {len(queryset)} 个DNS记录的检查任务')
    check_dns_now.short_description = '执行DNS检查'
