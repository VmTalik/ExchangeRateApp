from django.db import models


class ExchangeRate(models.Model):
    charcode = models.CharField(max_length=3, verbose_name='Код страны валюты', db_index=True)
    date = models.DateField(verbose_name='Дата курса валюты', db_index=True)
    rate = models.FloatField(verbose_name='Курс валюты')

    class Meta:
        verbose_name = 'Курс обмена валюты'
        verbose_name_plural = 'Курсы обмена валют'
