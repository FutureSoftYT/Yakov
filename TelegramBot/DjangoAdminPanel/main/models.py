from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    class Meta:
        verbose_name = 'Пользовател'
        verbose_name_plural = 'Пользователы'

    user_id = models.BigIntegerField(unique=True, verbose_name="Id Пользователя")
    username = models.CharField(max_length=400,blank=True,null=True, verbose_name="Username Пользователя")
    name = models.CharField(max_length=400,blank=True,null=True, verbose_name="Имя Пользователя")
    address = models.CharField(max_length=1000,unique=True, null=True, verbose_name="Адрес")
    twitter_name = models.CharField(unique=True, null=True,max_length=1000, verbose_name="Твиттер")
    balance = models.FloatField(default=0, blank=True,verbose_name="Баланс")
    refferals = models.IntegerField(default=0, verbose_name="Количество рефералов")
    tg = models.BooleanField(default=False, verbose_name="Задачи телеграм")
    twitter_tasks = models.BooleanField(default=False, verbose_name="Twitter репост")
    instagram = models.BooleanField(default=False, verbose_name="Instagram")
    joined_airdrop = models.BooleanField(default=False, verbose_name='Участвает в airdrop')

    def __str__(self):
        return str(self.user_id)

class Referral(TimeBasedModel):
    class Meta:
        verbose_name = 'Реферал'
        verbose_name_plural = 'Рефералы'
    user = models.BigIntegerField(unique=True, primary_key=True)
    referrer = models.BigIntegerField(blank = True,null=True)

