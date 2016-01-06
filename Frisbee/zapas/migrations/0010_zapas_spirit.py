# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0009_auto_20160106_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapas',
            name='spirit',
            field=models.BooleanField(default=True),
        ),
    ]
