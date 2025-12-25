from django import forms
from .models import WeightRecord

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['weight','comment']
