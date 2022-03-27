from django.contrib import admin

from django.db import transaction
from django.contrib import admin, messages
from dwscan.models import NMscannerModels, DNSBruteModels
# Register your models here.


@admin.register(NMscannerModels)
class NMScannerAdmin(admin.ModelAdmin):
    pass


@admin.register(DNSBruteModels)
class DnsBruteAdmin(admin.ModelAdmin):
    pass
