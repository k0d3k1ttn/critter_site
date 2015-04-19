# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('adopted', models.DateTimeField(blank=True, null=True)),
                ('fluffy', models.BooleanField()),
            ],
        ),
    ]
