from django.db import models

# Create your models here.
from authapp.models import UserProfile
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bug(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Fixed', 'Fixed'),
        ('Closed', 'Closed')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bugs_reported')
    assignee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bugs_assigned', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.description