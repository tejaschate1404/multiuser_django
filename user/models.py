from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('hr', 'HR'),
        ('reference_person', 'Reference Person'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return f"{self.username} - {self.role}"

# Model for HR Users
class HRProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='hr_profile')
    company_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile image for HR

    def __str__(self):
        return f"HR: {self.user.username} - {self.company_name}"

# Model for Employee Users
class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee_profile')
    description = models.TextField()

    def __str__(self):
        return f"Employee: {self.user.username}"

# Model for Reference Person (if needed)
class ReferencePersonProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='reference_profile')
    reference_details = models.TextField()

    def __str__(self):
        return f"Reference Person: {self.user.username}"

