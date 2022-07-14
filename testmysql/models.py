from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.lastname

