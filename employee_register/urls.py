from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), # get and post request for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), # get and post request for update operation
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), # get request to delete operation
    path('list/', views.employee_list, name='employee_list'), # get request to retrieve and display all records
]