# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taigaproject',
            name='default_priority',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='modified_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
