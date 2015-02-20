# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150220_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_id', models.BigIntegerField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('request_name', models.CharField(max_length=45, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
