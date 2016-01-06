# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0006_auto_20151129_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapas',
            name='tim_1',
            field=models.ForeignKey(related_name='tim', default=None, to='tim.Tim'),
        ),
        migrations.AlterField(
            model_name='zapas',
            name='tim_2',
            field=models.ForeignKey(related_name='zapas_tim', default=None, to='tim.Tim'),
        ),
    ]
