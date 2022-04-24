from django.db import models
from django.urls import reverse


class Address(models.Model):
    address = models.TextField('Content')

    def str(self):
        return self.address


class Work(models.Model):
    work = models.CharField('Work', max_length=50)
    time = models.TextField('Time')

    def str(self):
        return self.time


# class info(models.Model):
#     title = models.CharField('Name', max_length=60)
#     surname = models.TextField('Surname')
#     phone_num = models.IntegerField('Phone number')
#     email = models.EmailField('Email')
#     password = models.TextField('Password')
#     genre = models.CharField('Lovely genre', max_length=60)
#
#     def str(self):
#         return self.title
#     def get_absolute_url(self):
#         return f'/info/{self.id}'


class Registration(models.Model):
    name = models.CharField(max_length=15, )
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    tel_number = models.IntegerField(unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'
        ordering = ['name']
