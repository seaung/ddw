from django.contrib import admin

from django.db import transaction
from django.contrib import admin, messages
from dwscan.models import NMscannerResult, NMscannerTaskModels, DNSBruteTaskModels
# Register your models here.


@admin.register(NMscannerResult)
class NMScannerAdmin(admin.ModelAdmin):
    pass


@admin.register(DNSBruteTaskModels)
class DnsBruteAdmin(admin.ModelAdmin):
    pass
