import datetime

from django.db import models
from django.contrib.auth import get_user_model

from keywords.models import Keyword

User = get_user_model()

# Create your models here.
class CompanyEvent(models.Model):
    company = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    food = models.TextField()
    keywords = models.ManyToManyField(Keyword)


class Crawl(models.Model):
    date_time = models.DateTimeField(datetime.datetime(1970,1,1,0,0,0,0))