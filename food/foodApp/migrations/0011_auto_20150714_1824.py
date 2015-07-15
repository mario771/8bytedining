# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0010_auto_20150714_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuisines',
            old_name='cuisine',
            new_name='id_cuisine',
        ),
        migrations.RemoveField(
            model_name='cuisines',
            name='recipe_count',
        ),
    ]
