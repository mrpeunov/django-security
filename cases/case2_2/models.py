from django.db import models


class SupportServiceTicket(models.Model):
    text = models.CharField(max_length=128)
    file = models.FileField()
