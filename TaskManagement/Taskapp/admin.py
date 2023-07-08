from django.contrib import admin
from .models import User,Project,Comment,Task

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(User)
