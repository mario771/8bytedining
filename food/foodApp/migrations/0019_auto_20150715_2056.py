# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0018_auto_20150715_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='all_cuisines',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='all_recipes',
            field=models.TextField(default=''),
        ),
    ]
