# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0014_auto_20160106_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrac',
            name='datum_narodenia',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='hrac',
            name='miesto_bydliska',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hrac',
            name='telefonne_cislo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
