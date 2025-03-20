from django.db import models

# Create your models here.

class TarefaModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name