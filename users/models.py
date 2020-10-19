from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    class UserAccessChoice(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    role = models.CharField(
        max_length=20,
        choices=UserAccessChoice.choices,
        default=UserAccessChoice.USER
    )
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField('E-mail', unique=True)
    confirmation_code = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f' {self.role} : {self.email}'
