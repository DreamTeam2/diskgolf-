# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaj', '0007_auto_20151129_1541'),
        ('kategoria', '0002_auto_20151129_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriaTurnaju',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategoria', models.ForeignKey(to='kategoria.Kategoria')),
                ('turnaj', models.ForeignKey(to='turnaj.Turnaj')),
            ],
            options={
                'verbose_name_plural': 'Kategorie Turnajov',
            },
        ),
    ]
