# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0005_turnaj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnaj',
            name='report',
            field=models.CharField(default=b'', max_length=150, null=True, blank=True),
        ),
    ]
