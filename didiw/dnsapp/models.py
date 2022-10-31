from django.db import models

# Create your models here.


class DNSRecoders(models.Model):
    domain = models.CharField(max_length=50)


class DNSModels(models.Model):
    domain = models.CharField(max_length=50)
    enable = models.BooleanField()
    ip = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.domain


