from django.test import TestCase
from .models import Department, Employee

class BasicEmployeeTest(TestCase):
    def test_create_department_and_employee(self):
        dept = Department.objects.create(name="Engineering")
        emp = Employee.objects.create(first_name="John", last_name="Doe", email="john@example.com", department=dept)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(emp.department.name, "Engineering")
