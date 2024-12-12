from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)  # Title of the task
    detail = models.TextField()
    completed = models.BooleanField(default=False)  # Completion status
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update

    def __str__(self):
        return self.title
