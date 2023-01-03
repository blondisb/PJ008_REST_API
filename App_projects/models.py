from django.db import models

# Create your models here.
class MO_projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)