from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.HealthcareListView.as_view(),name='healthcare_list'),
    path('<int:pk>/',views.HealthcareDetailView.as_view(),name='healthcare_detail'),
    path('new/',views.HealthcareCreateView.as_view(),name = 'healthcare_create'),
    path('<int:pk>/edit/',views.HealthcareUpdateView.as_view(),name = 'healthcare_update'),
    ##name = はhmtl で使っているここをミスするとエラーが出た。2026年1月6日
    path('<int:pk>/delete/',views.HealthcareDeleteView.as_view(),name = 'healthcare_delete'),
    path('analytics/',views.HealthcareAnalyticsView.as_view(),name = 'healthcare_analytics'),
]
