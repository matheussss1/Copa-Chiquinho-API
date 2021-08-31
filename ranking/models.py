from django.db import models

# Create your models here.
class Jogador(models.Model):
    opcao_status = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    opcao_especialidade = [
        ('F', 'Front-end'),
        ('B', 'Back-end'),
        ('I', 'Infraestrutura'),
    ]

    nome = models.CharField(max_length=50, blank=False)
    especialidade = models.CharField(max_length=1, choices=opcao_especialidade)
    idade = models.IntegerField()
    sobre = models.TextField()
    status = models.CharField(max_length=1, choices=opcao_status, default='A')
    esta_devendo = models.BooleanField(default=True)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome