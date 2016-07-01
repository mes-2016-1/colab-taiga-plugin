# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taigaproject',
            name='default_priority',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 1, 3, 16, 20, 661051, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
