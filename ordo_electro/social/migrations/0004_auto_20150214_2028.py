# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150214_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='profile_image_url_https',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
    ]
