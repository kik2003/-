# -*- coding: utf-8 -*-
from django.db import models
import datetime
class Record(models.Model):
    name = models.CharField('Імя',max_length= 50)
    number = models.CharField('номер', max_length=10)
    time = models.TimeField('запис годни')
    data = models.DateField('запис дати',default=datetime.date.today)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'