# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0004_remove_hrac_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='klub',
            field=models.ForeignKey(default=1, to='klub.Klub'),
        ),
    ]
