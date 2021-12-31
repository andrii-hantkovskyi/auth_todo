from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
