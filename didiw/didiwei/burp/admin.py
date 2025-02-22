from django.contrib import admin
from django.utils.html import format_html
from .models import Burp, BurpResult
from .tasks import burp_scan_task


@admin.register(Burp)
class BurpAdmin(admin.ModelAdmin):
    list_display = ['name', 'target_url', 'ipaddr', 'scan_type', 'status_tag', 'risk_level', 'created_time', 'updated_time']
    list_filter = ['scan_status', 'scan_type', 'risk_level']
    search_fields = ['name', 'target_url', 'ipaddr', 'description']
    ordering = ['-created_time']
    
    def status_tag(self, obj):
        status_colors = {
            'pending': 'orange',
            'running': 'blue',
            'completed': 'green',
            'failed': 'red'
        }
        return format_html(
            '<span style="color: {};">●</span> {}',
            status_colors.get(obj.scan_status, 'gray'),
            obj.get_scan_status_display()
        )
    status_tag.short_description = '扫描状态'
    
    actions = ['start_scan_now']
    
    def start_scan_now(self, request, queryset):
        for burp in queryset:
            burp_scan_task.delay(burp.id)
        self.message_user(request, f'已触发 {len(queryset)} 个扫描任务')
    start_scan_now.short_description = '执行扫描'


@admin.register(BurpResult)
class BurpResultAdmin(admin.ModelAdmin):
    list_display = ['burp', 'ipaddr', 'port', 'vuln_type', 'verify_status_tag', 'created_time']
    list_filter = ['vuln_type', 'verify_status']
    search_fields = ['ipaddr', 'port', 'vuln_description', 'poc']
    ordering = ['-created_time']
    
    def verify_status_tag(self, obj):
        status_colors = {
            'unverified': 'orange',
            'verified': 'green',
            'false_positive': 'red'
        }
        return format_html(
            '<span style="color: {};">●</span> {}',
            status_colors.get(obj.verify_status, 'gray'),
            obj.get_verify_status_display()
        )
    verify_status_tag.short_description = '验证状态'
