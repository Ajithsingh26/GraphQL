from django.db import models

class Links(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
