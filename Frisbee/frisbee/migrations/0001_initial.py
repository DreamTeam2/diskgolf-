# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hrac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('krstne_meno', models.CharField(max_length=50, null=True, blank=True)),
                ('priezvisko', models.CharField(max_length=50, null=True, blank=True)),
                ('telefonne_cislo', models.CharField(max_length=50, null=True, blank=True)),
                ('pohlavie', models.CharField(default=b'Mu\xc5\xbe', max_length=5, null=True, blank=True, choices=[('Mu\u017e', 'Mu\u017e'), ('\u017dena', '\u017dena')])),
                ('datum_narodenia', models.DateField(default=datetime.date.today, null=True, blank=True)),
                ('miesto_bydliska', models.CharField(max_length=255, null=True, blank=True)),
                ('prezivka', models.CharField(max_length=50)),
                ('foto', models.CharField(default=b'', max_length=250, null=True, blank=True)),
                ('poznamka', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Hraci',
            },
        ),
        migrations.CreateModel(
            name='HracTimu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hrac', models.ForeignKey(to='frisbee.Hrac')),
            ],
            options={
                'verbose_name_plural': 'Hraci Timov',
            },
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='KategoriaTurnaju',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pocet_timov', models.PositiveSmallIntegerField(default=1, null=True, blank=True)),
                ('kategoria', models.ForeignKey(to='frisbee.Kategoria')),
            ],
            options={
                'verbose_name_plural': 'Kategorie Turnajov',
            },
        ),
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Kluby',
            },
        ),
        migrations.CreateModel(
            name='Tim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('umiestnenie', models.PositiveSmallIntegerField(default=1, null=True, blank=True)),
                ('nazov', models.CharField(default=b'', max_length=50)),
                ('spirit', models.BooleanField(default=True)),
                ('kategoria_turnaju', models.ForeignKey(to='frisbee.KategoriaTurnaju')),
                ('klub', models.ForeignKey(blank=True, to='frisbee.Klub', null=True)),
            ],
            options={
                'verbose_name_plural': 'Timy',
            },
        ),
        migrations.CreateModel(
            name='Turnaj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(max_length=50)),
                ('datum_od', models.DateField(default=datetime.date(2016, 2, 6), null=True, blank=True)),
                ('datum_do', models.DateField(default=datetime.date(2016, 2, 7), null=True, blank=True)),
                ('mesto', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('stat', models.CharField(default=b'', max_length=50, null=True, blank=True)),
                ('datum_zapisu', models.DateField(default=datetime.date.today, null=True, blank=True)),
                ('report', models.CharField(default=b'', max_length=150, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Turnaje',
            },
        ),
        migrations.CreateModel(
            name='Zapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vysledok_1', models.IntegerField()),
                ('vysledok_2', models.IntegerField()),
                ('kategoria_turnaju', models.ForeignKey(to='frisbee.KategoriaTurnaju')),
                ('tim_1', models.ForeignKey(related_name='tim', default=None, to='frisbee.Tim')),
                ('tim_2', models.ForeignKey(related_name='zapas_tim', default=None, to='frisbee.Tim')),
            ],
            options={
                'verbose_name_plural': 'Zapasy',
            },
        ),
        migrations.AddField(
            model_name='kategoriaturnaju',
            name='turnaj',
            field=models.ForeignKey(to='frisbee.Turnaj'),
        ),
        migrations.AddField(
            model_name='hractimu',
            name='tim',
            field=models.ForeignKey(to='frisbee.Tim'),
        ),
        migrations.AddField(
            model_name='hrac',
            name='klub',
            field=models.ForeignKey(blank=True, to='frisbee.Klub', null=True),
        ),
        migrations.AddField(
            model_name='hrac',
            name='uzivatel',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
