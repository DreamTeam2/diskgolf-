# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0004_zapas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapas',
            name='tim_1',
            field=models.ForeignKey(related_name='tim', blank=True, to='tim.Tim', null=True),
        ),
        migrations.AlterField(
            model_name='zapas',
            name='tim_2',
            field=models.ForeignKey(related_name='zapas_tim', blank=True, to='tim.Tim', null=True),
        ),
    ]
