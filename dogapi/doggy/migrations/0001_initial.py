# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseneeds', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1')),
                ('sheddingAmount', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1')),
                ('name', models.CharField(max_length=1000)),
                ('size', models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=1000)),
                ('friendliness', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('trainability', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('age', models.IntegerField(default=5)),
                ('gender', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=1000)),
                ('favoritefood', models.CharField(max_length=1000)),
                ('favoritetoy', models.CharField(max_length=1000)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doggy.breed')),
            ],
        ),
    ]
