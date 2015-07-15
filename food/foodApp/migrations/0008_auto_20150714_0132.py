# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0007_auto_20150714_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('recipe_count', models.IntegerField(default=0)),
                ('quant_data', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ing_id', models.CharField(default='', max_length=500)),
                ('name', models.CharField(default='', max_length=500)),
                ('recipe_count', models.IntegerField(default=0)),
                ('quant_data', models.CharField(default='', max_length=500)),
                ('nut_info', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('recipe_id', models.CharField(max_length=500)),
                ('directions', models.CharField(default='', max_length=5000)),
                ('img', models.CharField(max_length=500)),
                ('nut_info', models.CharField(max_length=5000)),
                ('quant_data', models.CharField(max_length=500)),
                ('cuisine', models.ForeignKey(to='foodApp.Cuisines')),
                ('ingredients', models.ManyToManyField(default='', to='foodApp.Ingredients')),
            ],
        ),
        migrations.RemoveField(
            model_name='stuff',
            name='thing',
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
        migrations.DeleteModel(
            name='Thing',
        ),
    ]
