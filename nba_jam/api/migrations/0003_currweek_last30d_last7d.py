# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-15 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_picks'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_games', models.FloatField()),
                ('total_bestbets', models.FloatField()),
                ('wins', models.FloatField()),
                ('losses', models.FloatField()),
                ('no_bets', models.FloatField()),
                ('best_bet_wins', models.FloatField()),
                ('date_range', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Last30d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_games', models.FloatField()),
                ('total_bestbets', models.FloatField()),
                ('wins', models.FloatField()),
                ('losses', models.FloatField()),
                ('no_bets', models.FloatField()),
                ('best_bet_wins', models.FloatField()),
                ('date_range', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Last7d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_games', models.FloatField()),
                ('total_bestbets', models.FloatField()),
                ('wins', models.FloatField()),
                ('losses', models.FloatField()),
                ('no_bets', models.FloatField()),
                ('best_bet_wins', models.FloatField()),
                ('date_range', models.CharField(max_length=100)),
            ],
        ),
    ]