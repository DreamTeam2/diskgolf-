# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0003_auto_20151129_1453'),
        ('tim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tim',
            name='turnaj',
        ),
        migrations.DeleteModel(
            name='Tim',
        ),
    ]
