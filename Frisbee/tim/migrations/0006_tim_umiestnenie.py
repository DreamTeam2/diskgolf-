# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0005_tim_klub'),
    ]

    operations = [
        migrations.AddField(
            model_name='tim',
            name='umiestnenie',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
    ]
