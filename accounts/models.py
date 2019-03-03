import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    last_crawl = models.DateTimeField(null=True, default=datetime.datetime(1970, 1,1,0,0,0,0))
    crawl_is_toggled = models.BooleanField(default=False)



