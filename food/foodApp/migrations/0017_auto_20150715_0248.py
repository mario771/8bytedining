# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0016_auto_20150715_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisines',
            name='ingr',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='cuisines',
            name='reci',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
