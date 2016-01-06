# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0002_auto_20151127_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnaj',
            name='mesto',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='turnaj',
            name='report',
            field=models.CharField(default=b'', max_length=150),
        ),
        migrations.AlterField(
            model_name='turnaj',
            name='stat',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
