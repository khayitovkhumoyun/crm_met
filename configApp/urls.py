from django.urls import path

from configApp.views import *

urlpatterns = [
    path('emp/<int:pk>/<int:month>/<str:year>/', EmployeeApi.as_view()),
    path('cus/<int:pk>/<int:month>/<str:year>/', CustomerApi.as_view()),
    path('emp/statistics/<int:month>/<str:year>/', EmployeesApi.as_view()),

]


