# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(null=True, default=None, max_length=100, blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date created')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name=b'Last date edited')),
                ('featuredimage', filebrowser.fields.FileBrowseField(help_text=b'This is the featured image.', max_length=200, null=True, verbose_name=b'Image', blank=True)),
                ('ingredients', models.TextField(default=None, null=True, blank=True)),
                ('method', models.TextField(default=None, null=True, blank=True)),
                ('sugarlevel', models.CharField(default=b'l', max_length=1, choices=[(b'l', b'Low'), (b'm', b'Medium'), (b'h', b'High')])),
                ('metatitle', models.CharField(default=None, max_length=120, null=True, blank=True)),
                ('metadescription', models.TextField(default=None, null=True, blank=True)),
                ('metakeywords', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('promoted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
