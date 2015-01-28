# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social_content', '0002_auto_20150127_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote_text',
            new_name='quote_text_small',
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_text_orig',
            field=models.TextField(default=datetime.datetime(2015, 1, 28, 7, 34, 9, 277316, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
