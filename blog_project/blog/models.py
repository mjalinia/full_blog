from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    owner = models.ForeignKey('auth.user',on_delete = models.CASCADE,)
    
    def __str__(self):
        return self.title