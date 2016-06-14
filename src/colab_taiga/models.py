from django.db import models


class TaigaProject(models.Model):
    type = u'project'
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
