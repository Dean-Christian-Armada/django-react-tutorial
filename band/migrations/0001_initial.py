# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('bio', models.TextField(null=True, blank=True)),
                ('image', models.CharField(unique=True, max_length=255)),
                ('date_added', models.DateField(default=datetime.datetime(2015, 10, 4, 10, 45, 1, 434080))),
            ],
        ),
    ]
