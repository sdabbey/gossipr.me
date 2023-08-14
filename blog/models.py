from django.db import models
from django.utils import timezone
# import random

class Post(models.Model):
    
    username = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_pics", blank=True)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.username
    