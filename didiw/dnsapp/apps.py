from django.apps import AppConfig
from django.contrib import admin, messages
from dnsapp.models import DNSModels, DNSRecoders
from django.db import transaction


class DnsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dnsapp'

