# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GRAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gr_author_id', models.IntegerField()),
                ('name', models.CharField(max_length=55)),
                ('image_url', models.CharField(max_length=255)),
                ('small_image_url', models.CharField(max_length=255)),
                ('author_page', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LimitStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_id', models.BigIntegerField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('request_name', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_text_small', models.CharField(max_length=140)),
                ('quote_text_orig', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_id', models.IntegerField()),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(default=b'', max_length=32)),
                ('account_id', models.BigIntegerField(default=0)),
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
            name='SocialAccountType',
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
                ('twitter_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('screen_name', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=25, null=True)),
                ('profile_location', models.CharField(max_length=45, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=160, null=True)),
                ('protected', models.BooleanField(default=False)),
                ('followers_count', models.IntegerField(default=0)),
                ('friends_count', models.IntegerField(default=0)),
                ('listed_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('favourites_count', models.IntegerField(default=0)),
                ('utc_offset', models.IntegerField(default=0, null=True)),
                ('time_zone', models.CharField(max_length=15, null=True)),
                ('geo_enabled', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('statuses_count', models.IntegerField(default=0)),
                ('lang', models.CharField(max_length=5, null=True)),
                ('profile_image_url_https', models.CharField(max_length=150, null=True)),
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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
        migrations.CreateModel(
            name='TwitterApiRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_id', models.BigIntegerField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('request_name', models.CharField(max_length=45, db_index=True)),
                ('request_status', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='twitteraccountrelationship',
            unique_together=set([('subject', 'target')]),
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='account_type',
            field=models.ForeignKey(to='social.SocialAccountType'),
            preserve_default=True,
        ),
    ]
