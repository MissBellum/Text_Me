from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TextBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    message = models.TextField(max_length=500, null=False)
    response = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
