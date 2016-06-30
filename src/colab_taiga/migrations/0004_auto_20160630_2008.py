# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0003_taigauser_taiga_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taigauser',
            name='taiga_projects',
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='owner',
            field=models.OneToOneField(related_name='own_projects', default=1, to='colab_taiga.TaigaUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='users',
            field=models.ManyToManyField(related_name='projects', to='colab_taiga.TaigaUser'),
            preserve_default=True,
        ),
    ]
