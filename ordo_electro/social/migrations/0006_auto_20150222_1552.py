# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150221_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccount',
            name='followers_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 22, 23, 52, 24, 925084, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='friends_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 22, 23, 52, 35, 860139, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
