from . import models
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import localtime
from .forms import HealthcareForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HealthcareListView(ListView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_list.html'
    context_object_name='healthcares'

class HealthcareDetailView(DetailView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_detail.html'
    context_object_name='healthcare'

class HealthcareCreateView(SuccessMessageMixin,CreateView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_create.html'
    # fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
    form_class = HealthcareForm
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「登録」されました。'

class HealthcareUpdateView(SuccessMessageMixin,UpdateView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_update.html'
    # fields = [    'physical_health','mental_health','eat_three_meals','exercise_time','sleep_time','weight','memo']
    form_class = HealthcareForm
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「更新」されました。'
    def form_valid(self, form):
        healthcare = form.save()
        print(f"記録日:'{healthcare.created}' 更新日:'{healthcare.updated}'")
        return super().form_valid(form)

class HealthcareDeleteView(SuccessMessageMixin,DeleteView):
    model = models.Healthcare
    template_name = 'weightapp_cbv/healthcare_confirm_delete.html'
    success_url = reverse_lazy('healthcare_list')
    success_message = '記録が「削除」されました。'