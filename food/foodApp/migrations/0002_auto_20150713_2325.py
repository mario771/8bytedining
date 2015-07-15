# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
