from django.db import models


class TaigaProject(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
