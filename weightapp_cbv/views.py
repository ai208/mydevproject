from . import models
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy


# Create your views here.
class HealthcareListView(ListView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_list.html'
    context_object_name='healthcares'

class HealthcareDetailView(DetailView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_detail.html'
    context_object_name='healthcare'

class HealthcareCreateView(CreateView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_create.html'
    fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
    success_url = reverse_lazy('healthcare_list')

