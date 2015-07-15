# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0006_auto_20150714_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='thing',
        ),
        migrations.AddField(
            model_name='stuff',
            name='thing',
            field=models.ManyToManyField(to='foodApp.Thing'),
        ),
    ]
