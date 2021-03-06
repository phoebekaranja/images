# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-05 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='problemStatement',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(default='lol', null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(default=True, to='epic.Categories'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epic.Location'),
        ),
    ]
