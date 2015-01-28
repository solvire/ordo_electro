# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('social_content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quote',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 7, 32, 42, 562026, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quote',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 7, 32, 51, 898882, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
