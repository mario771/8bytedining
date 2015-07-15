# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0008_auto_20150714_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='recipe_count',
        ),
    ]
