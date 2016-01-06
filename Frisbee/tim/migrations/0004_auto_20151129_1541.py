# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0003_tim'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tim',
            options={'verbose_name_plural': 'Timy'},
        ),
    ]
