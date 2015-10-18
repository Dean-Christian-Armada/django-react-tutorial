# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
