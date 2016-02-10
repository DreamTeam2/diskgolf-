# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategoriaTurnaju', '0001_initial'),
        ('zapas', '0007_auto_20151213_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zapas',
            name='turnaj',
        ),
        migrations.AddField(
            model_name='zapas',
            name='kategoria_turnaju',
            field=models.ForeignKey(default=1, to='kategoriaTurnaju.KategoriaTurnaju'),
        ),
    ]
