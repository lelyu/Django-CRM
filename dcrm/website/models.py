from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    
    # tostring method
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.state} {self.email}'

