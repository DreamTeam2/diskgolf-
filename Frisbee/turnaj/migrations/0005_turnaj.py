# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0004_delete_turnaj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnaj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(max_length=50)),
                ('datum_od', models.DateField(default=datetime.date.today)),
                ('datum_do', models.DateField(default=datetime.date.today)),
                ('spirit', models.BooleanField()),
                ('mesto', models.CharField(default=b'', max_length=50)),
                ('stat', models.CharField(default=b'', max_length=50)),
                ('datum_zapisu', models.DateField(default=datetime.date.today)),
                ('report', models.CharField(default=b'', max_length=150)),
            ],
        ),
    ]
