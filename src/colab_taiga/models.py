from django.db import models


class TaigaUser(models.Model):
    type = u'user'
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=140)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)


class TaigaProject(models.Model):
    type = u'project'
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    slug = models.TextField(blank=False, null=True)
    owner = models.ForeignKey(to=TaigaUser, related_name='own_projects')
    users = models.ManyToManyField(TaigaUser, related_name='projects')
    modified_date = models.DateTimeField()
    default_priority = models.IntegerField()