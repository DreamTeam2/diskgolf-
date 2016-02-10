# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0010_auto_20160106_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hrac',
            old_name='motorka',
            new_name='pohlavie',
        ),
    ]
