# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0012_auto_20160106_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='pohlavie',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', 'Mu\u017e'), (b'Female', 'Woman')]),
        ),
    ]
