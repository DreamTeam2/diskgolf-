# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0002_auto_20151129_1628'),
        ('tim', '0005_tim_klub'),
    ]

    operations = [
        migrations.CreateModel(
            name='HracTimu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hrac', models.ForeignKey(to='hrac.Hrac')),
                ('tim', models.ForeignKey(to='tim.Tim')),
            ],
            options={
                'verbose_name_plural': 'Hraci Timov',
            },
        ),
    ]
