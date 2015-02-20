# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_apirequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequest',
            name='request_status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
