# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hrac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('krstne_meno', models.CharField(max_length=50)),
                ('priezvisko', models.CharField(max_length=50)),
                ('prezivka', models.CharField(max_length=50)),
                ('foto', models.CharField(max_length=250, null=True, blank=True)),
                ('poznamka', models.CharField(max_length=250, null=True, blank=True)),
                ('klub', models.ForeignKey(to='klub.Klub')),
            ],
            options={
                'verbose_name_plural': 'Hraci',
            },
        ),
    ]
