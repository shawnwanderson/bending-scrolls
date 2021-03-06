# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('element', models.CharField(choices=[(b'WATER', b'WATER'), (b'EARTH', b'EARTH'), (b'FIRE', b'FIRE'), (b'AIR', b'AIR')], max_length=5)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', django_markdown.models.MarkdownField(blank=True)),
                ('book', models.CharField(blank=True, choices=[(b'WATER', b'Book 1: Water'), (b'EARTH', b'Book 2: Earth'), (b'FIRE', b'Book 3: Fire'), (b'AIR', b'Book 4: Air'), (b'SPIR', b'Book 5: Spirits'), (b'CHANG', b'Book 6: Change'), (b'BALA', b'Book 7: Balance')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Scroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('description', django_markdown.models.MarkdownField(blank=True)),
                ('inspirations', django_markdown.models.MarkdownField(blank=True)),
                ('element', models.CharField(choices=[(b'WATER', b'WATER'), (b'EARTH', b'EARTH'), (b'FIRE', b'FIRE'), (b'AIR', b'AIR')], max_length=5)),
                ('book', models.CharField(blank=True, choices=[(b'WATER', b'Book 1: Water'), (b'EARTH', b'Book 2: Earth'), (b'FIRE', b'Book 3: Fire'), (b'AIR', b'Book 4: Air'), (b'SPIR', b'Book 5: Spirits'), (b'CHANG', b'Book 6: Change'), (b'BALA', b'Book 7: Balance')], max_length=5)),
                ('image', models.ImageField(upload_to=b'')),
                ('benders', models.ManyToManyField(blank=True, to='scrolls.Bender')),
                ('episode', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='scrolls.Episode')),
                ('related_scrolls', models.ManyToManyField(blank=True, null=True, related_name='_scroll_related_scrolls_+', to='scrolls.Scroll')),
            ],
        ),
    ]
