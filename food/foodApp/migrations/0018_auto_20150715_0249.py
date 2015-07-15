# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0017_auto_20150715_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisines',
            name='ingr',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cuisines',
            name='reci',
            field=models.TextField(),
        ),
    ]
