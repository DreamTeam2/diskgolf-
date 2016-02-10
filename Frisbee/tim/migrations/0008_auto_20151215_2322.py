# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim', '0007_auto_20151215_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tim',
            name='kategoria_turnaju',
            field=models.ForeignKey(to='kategoriaTurnaju.KategoriaTurnaju'),
        ),
    ]
