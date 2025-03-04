from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student')
    )
    telegram_id = models.BigIntegerField(unique=True,blank=True,null=True)
    role = models.CharField(max_length=10,
                            choices=ROLES,
                            default='Student')
