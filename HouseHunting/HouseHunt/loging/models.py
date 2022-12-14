from django.db import models
from django.contrib.auth.hashers import make_password
from django.urls import reverse

# Create your models here.

class TenentUser(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GEN = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Prefer not to say'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100,null=False, default='adm123')
    gender = models.CharField(choices=GEN, max_length=20, default=OTHERS)

    def __str__(self):
        return self.first_name

    # def get_absolute_url(self):
    #     return reverse("loging/thank")
    

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(TenentUser, self).save(*args, **kwargs)

    emp_auth = models.Manager()