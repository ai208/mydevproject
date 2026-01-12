from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class WeightRecord(models.Model):
    weight = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=300)
    # アカウントを作ったときに付け足した。
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='weight_record'
    )
    def __str__(self):
        local_time = timezone.localtime(self.time)
        return f"{local_time:%Y-%m-%d %H:%M}_({self.weight}kg)"