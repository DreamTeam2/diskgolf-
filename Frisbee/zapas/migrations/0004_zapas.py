# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0005_turnaj'),
        ('tim', '0003_tim'),
        ('zapas', '0003_auto_20151129_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vysledok_1', models.IntegerField()),
                ('vysledok_2', models.IntegerField()),
                ('tim_1', models.ForeignKey(related_name='tim', default=-1, to='tim.Tim')),
                ('tim_2', models.ForeignKey(related_name='zapas_tim', default=-1, to='tim.Tim')),
                ('turnaj', models.ForeignKey(to='turnaj.Turnaj')),
            ],
        ),
    ]
