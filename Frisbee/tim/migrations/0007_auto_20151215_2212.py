# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategoriaTurnaju', '0001_initial'),
        ('tim', '0006_tim_umiestnenie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tim',
            name='turnaj',
        ),
        migrations.AddField(
            model_name='tim',
            name='kategoria_turnaju',
            field=models.ForeignKey(default=1, to='kategoriaTurnaju.KategoriaTurnaju'),
        ),
    ]
