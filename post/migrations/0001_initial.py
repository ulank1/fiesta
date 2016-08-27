# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('extra_phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('photo_url', models.URLField(max_length=100)),
                ('video_url', models.URLField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]