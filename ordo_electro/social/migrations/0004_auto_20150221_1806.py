# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150221_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccountrelationship',
            name='subject',
            field=models.ForeignKey(related_name='subject', verbose_name='subject', to_field=b'twitter_id', to='social.TwitterAccount'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteraccountrelationship',
            name='target',
            field=models.ForeignKey(related_name='target', verbose_name='target', to_field=b'twitter_id', to='social.TwitterAccount'),
            preserve_default=True,
        ),
    ]
