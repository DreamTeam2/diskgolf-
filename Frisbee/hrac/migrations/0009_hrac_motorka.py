# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0008_auto_20151215_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrac',
            name='motorka',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
