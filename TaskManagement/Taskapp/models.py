from django.db import models
from django.contrib.auth.models import AbstractUser , Group ,Permission

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('project_manager', 'Project Manager'),
        ('team_lead', 'Team Lead'),
        ('team_member', 'Team Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta(AbstractUser.Meta):
        pass

User._meta.get_field('groups').remote_field.related_name = 'taskapp_user_set'
User._meta.get_field('user_permissions').remote_field.related_name = 'taskapp_user_set'


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_projects')

class Task(models.Model):

    STATUS_CHOICES = (
    ("todo", "To Do"),
    ("in_progress", "In Progress"),
    ("completed", "Completed"),
)
    
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateField()    



class Comment(models.Model):
    comment_text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)    