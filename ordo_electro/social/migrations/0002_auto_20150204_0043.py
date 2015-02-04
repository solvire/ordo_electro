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
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(to='social.AccountType'),
            preserve_default=True,
        ),
    ]
