from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    id_number = models.CharField(max_length=11, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=256, blank=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Customer, self).save(*args, **kwargs)