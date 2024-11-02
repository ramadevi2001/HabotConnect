from django.db import models
from users.models import User  # Adjusted import for the custom User model

class Employee(models.Model):
    class Department(models.TextChoices):
        HR = "HR", "Human Resources"
        FINANCE = "Finance", "Finance"
        ENGINEERING = "Engineering", "Engineering"
        MARKETING = "Marketing", "Marketing"
        SALES = "Sales", "Sales"

    class Role(models.TextChoices):
        MANAGER = "Manager", "Manager"
        ENGINEER = "Engineer", "Engineer"
        INTERN = "Intern", "Intern"
        DIRECTOR = "Director", "Director"
        ASSISTANT = "Assistant", "Assistant"

    id = models.AutoField(primary_key=True)  # Unique identifier
    #user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the custom User model
    name = models.CharField(max_length=100)  # Employee name
    email = models.EmailField(unique=True)  # Unique email for the employee
    department = models.CharField(
        max_length=20,
        choices=Department.choices,
        default=Department.ENGINEERING
    )  # Department of the employee using enum
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ENGINEER
    )  # Role of the employee using enum
    date_joined = models.DateField(auto_now_add=True)  # Automatically set the date when the employee is created

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.name} - {self.role}"
