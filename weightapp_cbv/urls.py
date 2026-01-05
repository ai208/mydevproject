from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.HealthcareListView.as_view(),name='healthcare_list'),
    path('<int:pk>/',views.HealthcareDetailView.as_view(),name='healthcare_detail'),
]
