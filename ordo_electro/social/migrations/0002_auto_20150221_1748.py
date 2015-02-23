# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='location',
            field=models.CharField(max_length=45, null=True),
            preserve_default=True,
        ),
    ]
