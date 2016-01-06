# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0003_hrac_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrac',
            name='photo',
        ),
    ]
