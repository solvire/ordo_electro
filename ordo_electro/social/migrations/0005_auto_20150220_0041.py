# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20150214_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccountrelationship',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 20, 8, 41, 20, 628363, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='twitteraccountrelationship',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
