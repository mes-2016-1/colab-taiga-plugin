from django.db import models


class TaigaProject():
	title = models.TextField()
	description = models.TextField(blank=True, null=True)