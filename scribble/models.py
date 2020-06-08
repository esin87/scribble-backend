from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
