from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False)
    lastupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title