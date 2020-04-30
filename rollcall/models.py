from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

class Rollout(models.Model):
    time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    
class UserDetail(models.Model):
    NAME_MAX_LENGTH = 128
    
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE,
                             related_name='detail')
    personnel_code = models.CharField(max_length=10)
    manager_name = models.CharField(max_length=NAME_MAX_LENGTH)
    unit = models.CharField(max_length=32)
    