# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0015_auto_20150715_0242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuisines',
            old_name='id_cuisine',
            new_name='id_cusine',
        ),
    ]
