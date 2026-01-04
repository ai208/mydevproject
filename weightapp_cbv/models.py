from django.db import models

# Create your models here.
class Healthcare(models.Model):
    class five_point_scale(models.IntegerChoices):
        POOR = 1
        Fair = 2
        Good = 3
        Very_Good = 4
        Excellent = 5
    physical_health = models.IntegerField(choices=five_point_scale)
    mental_health = models.IntegerField(choices=five_point_scale)
    eat_three_meals = models.BooleanField(default=False)
    exercise_time = models.IntegerField()
    sleep_time = models.IntegerField()
    weight = models.FloatField()
    memo = models.TextField(null=True,blank=True,max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.created.strftime("%Y-%m-%d %H:%M")
    class Meta:
        ordering = ['-created']



