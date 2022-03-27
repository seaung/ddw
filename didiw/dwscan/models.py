from django.db import models

# Create your models here.


class NMscannerModels(models.Model):
    host = models.CharField('host', max_length=16)
    services = models.CharField('services', max_length=25)

    class Meta:
        db_table = 'nm_scanner'

    def __str__(self):
        return self.host

    def __unicode__(self):
        return self.host


class DNSBruteModels(models.Model):
    dns = models.CharField('dns', max_length=16)
    state = models.BooleanField('state')

    class Meta:
        db_table = 'dns_brute'

    def __str__(self):
        return self.dns

    def __unicode__(self):
        return self.dns
