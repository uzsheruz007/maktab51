from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=225, verbose_name="ism , familiya")
    teacher = models.CharField(max_length=225, verbose_name="Mavzu")
    messages = models.TextField(max_length=225, verbose_name="Mesagges", null=True)

    number = models.CharField(max_length=225, verbose_name="Telefon nomer")

    def __str__(self):
        return self.surname


class Contact(models.Model):
    name = models.CharField(max_length=225,  verbose_name=" Name ")
    email = models.EmailField(max_length=225, verbose_name="Email")
    subject = models.CharField( max_length=50, verbose_name="Subject")
    messages = models.TextField(max_length=225, verbose_name="Mesagges", null=True)

    def __str__(self):
        return self.name
    
class login(models.Model):
    email = models.EmailField(max_length=225, verbose_name="Email")
    subject = models.CharField( max_length=50, verbose_name="Password")

    def __str__(self):
        return self.email