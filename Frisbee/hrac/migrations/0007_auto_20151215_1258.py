# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0006_auto_20151212_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='foto',
            field=models.CharField(default=b'https://secure.gravatar.com/avatar/ad516503a11cd5ca435acc9bb6523536?s=320', max_length=250, null=True, blank=True),
        ),
    ]
