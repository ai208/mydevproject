from django.db import models
from django.utils import timezone
# Create your models here.
class WeightRecord(models.Model):
    weight = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=300)
    def __str__(self):
        local_time = timezone.localtime(self.time)
        return f"{local_time:%Y-%m-%d %H:%M}_({self.weight}kg)"