from django.db import models
from django.contrib.auth.models import User

# Task model
# This model represents a task in the system.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'),
                                       ('completed', 'Completed'),
                                       ('archived', 'Archived')],
                                       default='pending')
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, 
                                    related_name='assigned_tasks')
    verified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='verified_tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Group model
# This model represents a group in the system. Keep friends accountable.
class Group(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='groups')

class Picture(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    picture_url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)