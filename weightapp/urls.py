from django.urls import path
from . import views

urlpatterns = [
    path('',views.weight_list,name='weight_list'),
    path('<int:pk>/',views.weight_detail,name='weight_detail'),
    path('new/',views.weight_create,name = 'weight_create'),
    path('<int:pk>/edit/',views.weight_update, name='weight_update'),
    path('<int:pk>/delete/',views.weight_delete, name='weight_delete'),
]