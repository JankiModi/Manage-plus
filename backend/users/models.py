from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('COMMITTEE', 'Society Committee'),
        ('RESIDENT', 'Resident'),
        ('SECURITY', 'Security'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Add these lines to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

    def is_committee(self):
        return self.user_type == 'COMMITTEE'

    def is_resident(self):
        return self.user_type == 'RESIDENT'

    def is_security(self):
        return self.user_type == 'SECURITY'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"