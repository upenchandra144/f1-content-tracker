from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = [
        ("EDITOR", "Editor"),
        ("VIEWER", "Viewer"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    display_name = models.CharField(
        max_length=100
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="VIEWER"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.display_name} ({self.role})"