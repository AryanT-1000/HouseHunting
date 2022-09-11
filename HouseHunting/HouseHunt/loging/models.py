from django.db import models


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
    gender = models.CharField(choices=GEN, max_length=20, default=MALE)

    def __str__(self):
        return self.first_name