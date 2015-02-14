# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_id', models.IntegerField()),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(default=b'', max_length=32)),
                ('active', models.BooleanField(default=True)),
                ('token', models.CharField(max_length=128)),
                ('secret', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('screen_name', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=25)),
                ('profile_location', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=160)),
                ('protected', models.BooleanField(default=False)),
                ('followers_count', models.IntegerField()),
                ('friends_count', models.IntegerField()),
                ('listed_count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('favourites_count', models.IntegerField()),
                ('utc_offset', models.IntegerField()),
                ('time_zone', models.CharField(max_length=15)),
                ('geo_enabled', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('statuses_count', models.IntegerField()),
                ('lang', models.CharField(max_length=5)),
                ('profile_image_url_https', models.CharField(max_length=15)),
                ('following', models.BooleanField(default=False)),
                ('follow_request_sent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterAccountRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now=True)),
                ('subject', models.ForeignKey(related_name='subject', verbose_name='subject', to='social.TwitterAccount')),
                ('target', models.ForeignKey(related_name='target', verbose_name='target', to='social.TwitterAccount')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Twitter Relationship',
                'verbose_name_plural': 'Twitter Relationships',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='twitteraccountrelationship',
            unique_together=set([('subject', 'target')]),
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(to='social.AccountType'),
            preserve_default=True,
        ),
    ]
