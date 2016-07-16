import random
import string
from django.core.urlresolvers import reverse
from django.test import TestCase
from employee.models import Employee


def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

class EmployeeTest(TestCase):

    def test_list(self):
        response = self.client.get(reverse('employee'))
        self.assertEqual(response.status_code, 200)

    def create_employee(self):
        name = ' '.join([randomword(10).title(), randomword(10).title()])
        email = ''.join([randomword(10), '@', randomword(10), '.com'])
        department = randomword(20).title()
        return Employee.objects.create(
            name=name,
            email=email,
            department=department
        )

    def test_employee_creation(self):
        employee = self.create_employee()
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.name)


    def test_employee_list(self):
        employee = self.create_employee()
        url = reverse('employee')
        data = {
            'name' : employee.name,
            'email' : employee.email,
            'department' : employee.department
        }
        response = self.client.get(url, {'name': data.get('name')})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url, {'email': data.get('email')})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
