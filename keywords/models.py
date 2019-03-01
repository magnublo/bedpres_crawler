from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Keyword(models.Model):
    value = models.TextField(max_length=200, default='foobar')
    user = models.ForeignKey(User, models.CASCADE, default=1)

    def __str__(self):
        return self.value
