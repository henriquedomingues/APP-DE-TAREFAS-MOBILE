from django.db import models

# Create your models here.

class tblusuarios(models.Model):
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=128, null=False)


class tbltarefas(models.Model):

    status_choice = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),   
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=180, null=False)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    data_criacao = models.DateTimeField(null=False, auto_now_add=True)
    status = models.CharField(max_length=50, null=False, choices=status_choice, default='pendente')