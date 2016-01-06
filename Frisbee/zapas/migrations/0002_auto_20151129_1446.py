# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0001_initial'),
        ('zapas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapas',
            name='tim_1',
            field=models.ForeignKey(related_name='tim', default=-1, to='tim.Tim'),
        ),
        migrations.AlterField(
            model_name='zapas',
            name='tim_2',
            field=models.ForeignKey(related_name='zapas_tim', default=-1, to='tim.Tim'),
        ),
    ]
