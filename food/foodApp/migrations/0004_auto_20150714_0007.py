# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0003_auto_20150714_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='stuff',
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
    ]
