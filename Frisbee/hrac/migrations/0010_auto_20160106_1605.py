# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0009_hrac_motorka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='motorka',
            field=models.CharField(max_length=5, null=True, choices=[(b'Male', b'Man'), (b'Female', b'Woman')]),
        ),
    ]
