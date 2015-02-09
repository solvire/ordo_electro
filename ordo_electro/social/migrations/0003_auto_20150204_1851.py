# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150204_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
    ]
