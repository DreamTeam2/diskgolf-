# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0001_initial'),
        ('turnaj', '0003_auto_20151129_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vysledok_1', models.IntegerField()),
                ('vysledok_2', models.IntegerField()),
                ('tim_2', models.ForeignKey(to='tim.Tim')),
                ('turnaj', models.ForeignKey(to='turnaj.Turnaj')),
            ],
        ),
    ]
