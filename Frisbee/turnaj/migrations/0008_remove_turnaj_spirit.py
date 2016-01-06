# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0007_auto_20151129_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnaj',
            name='spirit',
        ),
    ]
