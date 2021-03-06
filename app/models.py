from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_client = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    phone = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.username


choice = (
    ('done', 'DONE'),
    ('pending', 'PENDING')
)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50, blank=True)
    task_description = models.TextField(max_length=150, blank=True)
    status = models.CharField(max_length=50, default='pending', choices=choice, null=False)
    completion_date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.task_name


