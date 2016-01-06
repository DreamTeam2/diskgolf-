# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0007_auto_20151215_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='foto',
            field=models.CharField(default=b'', max_length=250, null=True, blank=True),
        ),
    ]
