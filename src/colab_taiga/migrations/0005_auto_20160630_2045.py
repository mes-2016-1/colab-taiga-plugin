# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0004_auto_20160630_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taigaproject',
            name='owner',
            field=models.ForeignKey(related_name='own_projects', to='colab_taiga.TaigaUser'),
            preserve_default=True,
        ),
    ]
