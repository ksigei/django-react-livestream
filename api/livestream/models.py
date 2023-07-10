from django.db import models
from django.contrib.auth.models import User


class Livestream(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)
    viewers = models.ManyToManyField(User)

class Comment(models.Model):
    livestream = models.ForeignKey(Livestream, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)