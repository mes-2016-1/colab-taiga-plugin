# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab_taiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaigaUserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.TextField(null=True, blank=True)),
                ('total_points', models.TextField(null=True, blank=True)),
                ('milestone', models.TextField(null=True, blank=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(related_name='own_userstory', to='colab_taiga.TaigaUser', null=True)),
                ('project', models.ForeignKey(to='colab_taiga.TaigaProject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
