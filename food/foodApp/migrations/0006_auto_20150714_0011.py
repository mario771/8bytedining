# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0005_auto_20150714_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='stuff',
        ),
        migrations.AddField(
            model_name='stuff',
            name='thing',
            field=models.ForeignKey(default='', to='foodApp.Thing'),
        ),
    ]
