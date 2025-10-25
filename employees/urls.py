from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health_check, name="health"),
    path("departments/", views.DepartmentListCreateAPIView.as_view(), name="department-list-create"),
    path("departments/<int:pk>/", views.DepartmentRetrieveUpdateDestroyAPIView.as_view(), name="department-detail"),
    path("employees/", views.EmployeeListCreateAPIView.as_view(), name="employee-list-create"),
    path("employees/<int:employee_id>/", views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name="employee-detail"),
]
