# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrac',
            name='uzivatel',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='hrac',
            name='klub',
            field=models.ForeignKey(blank=True, to='klub.Klub', null=True),
        ),
    ]
