# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaigaProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                 auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
