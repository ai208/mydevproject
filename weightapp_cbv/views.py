from . import models
from django.views.generic import ListView,DetailView


# Create your views here.
class HealthcareListView(ListView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_list.html'
    context_object_name='healthcares'

class HealthcareDetailView(DetailView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_detail.html'
    context_object_name='healthcare'