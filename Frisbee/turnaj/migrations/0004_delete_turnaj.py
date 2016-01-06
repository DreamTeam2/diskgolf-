# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0003_auto_20151129_1453'),
        ('tim', '0002_auto_20151129_1453'),
        ('turnaj', '0003_auto_20151129_1413'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Turnaj',
        ),
    ]
