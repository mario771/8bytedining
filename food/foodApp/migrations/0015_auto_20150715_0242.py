# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0014_remove_recipes_cuisine_ori'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisines',
            name='ingr',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='cuisines',
            name='reci',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='recipes',
            name='cuisine_ori',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
