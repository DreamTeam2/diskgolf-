# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0005_auto_20151212_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='klub',
            field=models.ForeignKey(blank=True, to='klub.Klub', null=True),
        ),
    ]
