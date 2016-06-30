# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaigaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                 serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=140)),
                ('bio', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
