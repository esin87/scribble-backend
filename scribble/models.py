from django.db import models
from users.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    body = models.TextField()
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
