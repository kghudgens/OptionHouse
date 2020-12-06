from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    date  = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return f'{self.title}'