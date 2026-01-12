from django.db import models
# 2026年1月9日　ch9
import pandas as pd
from django_pandas.io import read_frame
from django.conf import settings # アカウントの時に付け足した。
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
    # アカウントの時に付け足した。
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='healthcare_record'
    )
    def __str__(self):
        return self.created.strftime("%Y-%m-%d %H:%M")
    class Meta:
        ordering = ['-created']

    @classmethod
    def get_eat_three_meals_rate(cls):
        healthcares = cls.objects.all()
        eat_three = healthcares.filter(eat_three_meals=True).count()
        not_eat_three = healthcares.filter(eat_three_meals=False).count()
        total = eat_three + not_eat_three

        if  total > 0:
            eat_three_meal_rate = round((eat_three/total)*100,2)
        else:
            eat_three_meal_rate = 0
        return{
            'eat_three':eat_three,
            'not_eat_three':not_eat_three,
            'total':total,
            'eat_three_meal_rate':eat_three_meal_rate
        }
    @classmethod
    def get_healthcares_dataframe(cls):
        #データフレームへ
        # healthcares = cls.objects.all()
        # return read_frame(healthcares)
        # AIに教えてもらった方法　1~5で取得する方法
        qs = cls.objects.all()
        # verbose=False にすることで、Label(非常に良い)ではなくValue(1)を取得します
        df = read_frame(qs, verbose=False)
        return df