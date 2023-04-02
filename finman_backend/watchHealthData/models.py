from django.db import models
from django.db.models import fields
from ..users.models import User
# Create your models here.


class WatchHealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_health_data')
    watch_id = fields.CharField(max_length=50)
    time = fields.DateTimeField(auto_now_add=True)
    value = fields.FloatField()
    type = fields.CharField(max_length=20)



