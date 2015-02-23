# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150221_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='time_zone',
            field=models.CharField(max_length=35, null=True),
            preserve_default=True,
        ),
    ]
