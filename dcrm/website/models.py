from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    