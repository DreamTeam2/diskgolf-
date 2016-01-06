# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0002_auto_20151129_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrac',
            name='photo',
            field=models.ImageField(upload_to=b'path/', blank=True),
        ),
    ]
