from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=300, null=False)
    is_login = models.BooleanField(default=False)
    HOSPITAL_CHOICES = (
        ('SEOUL','서울대학병원'),
        ('INHA', '인하대학병원'),
        ('YONSEI', '연세세브란스병원')
    )

    hospital = models.CharField(max_length=10, choices=HOSPITAL_CHOICES, default='INHA')