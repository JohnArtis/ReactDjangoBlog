from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    