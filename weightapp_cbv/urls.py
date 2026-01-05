from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.HealthcareListView.as_view(),name='healthcare_list'),
    path('<int:pk>/',views.HealthcareDetailView.as_view(),name='healthcare_detail'),
    path('new/',views.HealthcareCreateView.as_view(),name = 'healthcare_create'),
]
