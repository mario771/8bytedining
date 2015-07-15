# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0011_auto_20150714_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredient_amount',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
