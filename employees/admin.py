from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "first_name", "last_name", "email", "department", "designation", "salary", "hire_date", "is_active")
    list_filter = ("department", "is_active")
    search_fields = ("first_name", "last_name", "email", "designation")
