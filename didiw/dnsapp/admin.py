from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import DNSModels, DNSRecoders


admin.site.site_header = "敌敌畏"
admin.site.site_title = "敌敌畏后台"
admin.site.index_title = "敌敌畏dns"


admin.register(DNSModels)
admin.register(DNSRecoders)
