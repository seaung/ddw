from django.db import models

# Create your models here.

status_choices = (
        (0, 'pending'),
        (1, 'running'),
        (2, 'failure'),
        (3, 'success'),
)

class NMscannerTaskModels(models.Model):
    host = models.CharField('host', max_length=16)
    status = models.CharField('status', choices=status_choices, max_length=2)

    class Meta:
        db_table = 'nm_scanner'

    def __str__(self):
        return self.host

    def __unicode__(self):
        return self.host


class NMscannerResult(models.Model):
    pass


class DNSBruteTaskModels(models.Model):
    dns = models.CharField('dns', max_length=16)
    state = models.BooleanField('state')

    class Meta:
        db_table = 'dns_brute'

    def __str__(self):
        return self.dns

    def __unicode__(self):
        return self.dns


class DNSBruteResult(models.Model):
    pass
