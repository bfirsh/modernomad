# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-23 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_userprofile_primary_accounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backing',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Resource'),
        ),
        migrations.AlterField(
            model_name='location',
            name='readonly_admins',
            field=models.ManyToManyField(blank=True, help_text=b'Readonly admins do not show up as part of the community. Useful for eg. external bookkeepers, etc.', related_name='readonly_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='primary_accounts',
            field=models.ManyToManyField(blank=True, help_text=b'one for each currency', related_name='primary_for', to='bank.Account'),
        ),
    ]