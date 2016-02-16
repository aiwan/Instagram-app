# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_name', models.CharField(max_length=200)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_gallery.User')),
            ],
        ),
    ]