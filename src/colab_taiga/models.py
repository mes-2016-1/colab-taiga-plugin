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


class TaigaUserStory(models.Model):
    type = u'userstory'
    subject = models.TextField(blank=True, null=True)
    total_points = models.TextField(blank=True, null=True)
    milestone = models.TextField(blank=True, null=True)
    assigned_to = models.TextField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    project = models.ForeignKey(TaigaProject, on_delete=models.CASCADE)
