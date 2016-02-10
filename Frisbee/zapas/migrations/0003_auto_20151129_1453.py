# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0002_auto_20151129_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zapas',
            name='tim_1',
        ),
        migrations.RemoveField(
            model_name='zapas',
            name='tim_2',
        ),
        migrations.RemoveField(
            model_name='zapas',
            name='turnaj',
        ),
        migrations.DeleteModel(
            name='Zapas',
        ),
    ]
