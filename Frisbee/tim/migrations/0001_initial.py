# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0003_auto_20151129_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(default=b'', max_length=50)),
                ('turnaj', models.ForeignKey(to='turnaj.Turnaj')),
            ],
        ),
    ]
