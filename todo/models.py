from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = 'P', 'Pendente'
        DONE = 'D', 'Concluída'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=Status.choices,default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title