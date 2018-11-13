# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-12 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField()),
                ('rank', models.FloatField()),
                ('game_id', models.CharField(max_length=15)),
                ('away_team', models.CharField(max_length=3)),
                ('home_team', models.CharField(max_length=3)),
                ('vegas_spread_str', models.CharField(max_length=20)),
                ('pred_spread_str', models.CharField(max_length=20)),
                ('pick_str', models.CharField(max_length=20)),
                ('best_bet', models.CharField(max_length=3)),
            ],
        ),
    ]
