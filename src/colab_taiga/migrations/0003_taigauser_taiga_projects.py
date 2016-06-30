# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0002_taigauser'),
    ]

    operations = [
        migrations.AddField(
            model_name='taigauser',
            name='taiga_projects',
            field=models.ManyToManyField(to='colab_taiga.TaigaProject'),
            preserve_default=True,
        ),
    ]
