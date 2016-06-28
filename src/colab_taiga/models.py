from django.db import models


class TaigaProject(models.Model):
    type = u'project'
    title = models.TextField()
    description = models.TextField(blank=True, null=True)


class TaigaUser(models.Model):
    type = u'user'
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=140)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)
    taiga_projects = models.ManyToManyField(TaigaProject)
