# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_secrets', '0002_auto_20170530_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='message_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='author',
        ),
        migrations.AddField(
            model_name='message',
            name='likers',
            field=models.ManyToManyField(related_name='likedsecrets', to='dojo_secrets.User'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
