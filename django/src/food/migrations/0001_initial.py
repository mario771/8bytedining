# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cusine',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('cusine_id', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('recipe_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('recipe_id', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('cusine', models.CharField(max_length=500)),
                ('cooking_method', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('thumb', models.CharField(max_length=500)),
            ],
        ),
    ]
