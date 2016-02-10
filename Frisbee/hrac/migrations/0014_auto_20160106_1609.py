# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0013_auto_20160106_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='pohlavie',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', 'Mu\u017e'), (b'Female', '\u017dena')]),
        ),
    ]
