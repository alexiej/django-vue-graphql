from django.db import models
from django.contrib import admin

# Create your models here.

class Task(models.Model):
    isDone = models.BooleanField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  	pass