from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from .models import Employee, User
from rest_framework_simplejwt.tokens import RefreshToken

class TestSetup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.token = RefreshToken.for_user(self.user).access_token

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

class CreateEmployeeTest(TestSetup):
    def test_create_employee(self):
        self.authenticate()
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'department': 'Engineering',
            'role': 'Engineer'
        }
        response = self.client.post(reverse('employee-list-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GetEmployeeTest(TestSetup):
    def test_get_all_employees(self):
        self.authenticate()
        response = self.client.get(reverse('employee-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_by_id(self):
        self.authenticate()
        employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="Engineering",
            role="Engineer"
        )
        response = self.client.get(reverse('employee-detail', kwargs={'pk': employee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], employee.name)

class UpdateEmployeeTest(TestSetup):
    def test_update_employee(self):
        self.authenticate()
        employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="Engineering",
            role="Engineer"
        )
        data = {'name': 'John Smith'}
        response = self.client.patch(reverse('employee-detail', kwargs={'pk': employee.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        employee.refresh_from_db()
        self.assertEqual(employee.name, 'John Smith')

class DeleteEmployeeTest(TestSetup):
    def test_delete_employee(self):
        self.authenticate()
        employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            department="Engineering",
            role="Engineer"
        )
        response = self.client.delete(reverse('employee-detail', kwargs={'pk': employee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FilterEmployeeTest(TestSetup):
    def test_filter_employees_by_department(self):
        self.authenticate()
        Employee.objects.create(name="Alice", email="alice@example.com", department="HR", role="Manager")
        Employee.objects.create(name="Bob", email="bob@example.com", department="Engineering", role="Engineer")
        response = self.client.get(reverse('employee-list-create') + '?department=Engineering')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Assuming pagination with default page size

class PaginationTest(TestSetup):
    def test_pagination(self):
        self.authenticate()
        for i in range(15):
            Employee.objects.create(name=f"Employee {i}", email=f"employee{i}@example.com", department="Engineering", role="Engineer")
        response = self.client.get(reverse('employee-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Default page size of 2
