# Generated by Django 4.0.2 on 2022-02-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_airdrop',
            field=models.BooleanField(default=False, verbose_name='Участвает в airdrop'),
        ),
    ]
