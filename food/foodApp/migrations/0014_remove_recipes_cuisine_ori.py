# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0013_recipes_cuisine_ori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='cuisine_ori',
        ),
    ]
