from django.urls import path
from . import views

app_name = 'patient'

urlpatterns= [
    path('list/', views.patient_list, name='list'),
    path('add/', views.patient_add, name='add'),
    path('patient_common/',views.patient_common, name='patient_common'),
    path('patient_detail/<int:pk>', views.patient_detail, name='patient_detail'),
    path('patient_detail/search/', views.search_results, name='search_results'),
]