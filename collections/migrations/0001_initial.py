# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = [
    ]
    
    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serilize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('record_name', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collections.Collection')),
            ],
            options={
                'ordering': ['collection', 'record_number'],
            },
        ),
    ]
