from django import forms
from .models import Healthcare

class HealthcareForm(forms.ModelForm):
    class Meta:
        model = Healthcare
        fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
        labels = {
            'physical_health':'本日の体調を5段階で評価してください。',
            'mental_health':'本日の精神状態を5段階で評価してください。',
            'eat_three_meals':'前日三食すべて食べましたか？',
            'exercise_time':'本日の運動時間(分)',
            'sleep_time':'本日の睡眠時間(時間)',
            'weight':'本日の体重(kg)',
            'memo':'本日の振り返り',
        }