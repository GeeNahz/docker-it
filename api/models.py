from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True)

class Todo(models.Model):
    title = models.CharField(max_length=244, null=False, blank=False, db_index=True)
    is_complete = models.BooleanField(default=False, db_index=True)