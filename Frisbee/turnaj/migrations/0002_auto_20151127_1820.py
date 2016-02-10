# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnaj',
            name='datum_zapisu',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='turnaj',
            name='mesto',
            field=models.CharField(default=b'null', max_length=50),
        ),
        migrations.AddField(
            model_name='turnaj',
            name='report',
            field=models.CharField(default=b'null', max_length=150),
        ),
        migrations.AddField(
            model_name='turnaj',
            name='stat',
            field=models.CharField(default=b'null', max_length=50),
        ),
        migrations.AlterField(
            model_name='turnaj',
            name='datum_do',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='turnaj',
            name='datum_od',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
