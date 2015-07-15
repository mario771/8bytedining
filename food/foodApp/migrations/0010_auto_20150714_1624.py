# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0009_remove_ingredients_recipe_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='nut_info',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='nut_info',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
