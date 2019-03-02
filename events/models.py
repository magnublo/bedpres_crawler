from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CompanyEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.TextField()
    date = models.DateField()
    time = models.TimeField()