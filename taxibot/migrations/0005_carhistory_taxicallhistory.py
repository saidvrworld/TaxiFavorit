# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-07 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxibot', '0004_auto_20170304_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=200)),
                ('car_number', models.CharField(max_length=20)),
                ('car_time', models.IntegerField(default=0)),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxibot.TaxiCall')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiCallHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_id', models.IntegerField(default=0)),
                ('IsMap', models.BooleanField(default=False)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('address', models.CharField(default='None', max_length=500)),
                ('type', models.CharField(default='None', max_length=100)),
                ('number', models.CharField(default='None', max_length=20)),
                ('details', models.CharField(default='None', max_length=500)),
                ('call_time', models.TimeField()),
                ('call_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
