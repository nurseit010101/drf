from tabnanny import verbose
from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name = 'Имя')
    last_name = models.CharField(max_length = 70, verbose_name = 'Фамилия')
    age = models.IntegerField(verbose_name = 'Возраст студента')
    gender = models.CharField(max_length = 50, verbose_name = 'Пол студента')
    course = models.CharField(max_length = 50, verbose_name = 'Курс')