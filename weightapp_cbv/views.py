from . import models
from django.views.generic import ListView


# Create your views here.
class HealthcareListView(ListView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_list.html'
    context_object_name='healthcares'