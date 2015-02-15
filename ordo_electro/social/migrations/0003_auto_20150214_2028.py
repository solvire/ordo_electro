# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150214_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='utc_offset',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
