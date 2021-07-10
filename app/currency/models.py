from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)
    


class ContactUs(models.Model):
    email_from = models.CharField(max_length=64)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)


class Source(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
