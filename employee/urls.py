from django.urls import path
from . import views

urlpatterns = [
    path('', views.employe_list, name='employee_list'),
    path('<int:id>/details/', views.employe_details, name='employee_details'),
    path('add/', views.employee_add, name='employee_add'),
    path('<int:id>/edit/', views.employe_edit, name='employee_edit'),
    path('<int:id>/delete/', views.employe_delete, name='employee_delete'),
    path('profile/', views.profile, name='my_profile'),
    
    
]
