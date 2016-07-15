from django.test import TestCase
from employee.models import Employee

# models test
class EmployeeTest(TestCase):

    def create_employee(self, name="Tester",email="test@test.com",
                        department='Department of Tests'):
        return Employee.objects.create(
            name=name,
            email=email,
            department=department
        )

    def test_employee_creation(self):
        employee = self.create_employee()
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.name)
