# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapas', '0008_auto_20151215_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapas',
            name='kategoria_turnaju',
            field=models.ForeignKey(to='kategoriaTurnaju.KategoriaTurnaju'),
        ),
    ]
