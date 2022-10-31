from django.contrib import admin

# Register your models here.

from django.contrib import admin, messages
from dnsapp.models import DNSRecoders, DNSModels


admin.site.site_header = "DNS"


@admin.register(DNSModels)
class DNSScanner(admin.ModelAdmin):
    pass


@admin.register(DNSRecoders)
class DNSRecoder(admin.ModelAdmin):
    pass
