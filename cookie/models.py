from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Cookie(models.Model):
    value = models.TextField(max_length=200)
    user = models.OneToOneField(User, models.PROTECT)

    def __str__(self):
        return self.value
