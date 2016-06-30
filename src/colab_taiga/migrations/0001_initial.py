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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaigaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=140)),
                ('bio', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='owner',
            field=models.ForeignKey(related_name='own_projects', to='colab_taiga.TaigaUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taigaproject',
            name='users',
            field=models.ManyToManyField(related_name='projects', to='colab_taiga.TaigaUser'),
            preserve_default=True,
        ),
    ]
