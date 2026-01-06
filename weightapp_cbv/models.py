from django.db import models

# Create your models here.
class Healthcare(models.Model):
    class five_point_scale(models.IntegerChoices):
        # 日本語で用意しておくと、formで日本語でになる。
        # poor python の定数、1 dbの値、'非常に悪い' label 人間用　AIに教えてもらった。
        POOR = 1, '非常に悪い'
        FAIR = 2, '悪い'
        GOOD = 3, '普通'
        VERY_GOOD = 4, '良い'
        EXCELLENT = 5, '非常に良い'
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



