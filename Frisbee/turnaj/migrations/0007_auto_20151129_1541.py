# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0006_auto_20151129_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turnaj',
            options={'verbose_name_plural': 'Turnaje'},
        ),
    ]
