# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klub', '0001_initial'),
        ('tim', '0004_auto_20151129_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='tim',
            name='klub',
            field=models.ForeignKey(blank=True, to='klub.Klub', null=True),
        ),
    ]
