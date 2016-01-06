# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0005_auto_20151129_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zapas',
            options={'verbose_name_plural': 'Zapasy'},
        ),
    ]
