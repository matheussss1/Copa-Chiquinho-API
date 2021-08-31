from django.db import models
import os, shutil
# Create your models here.
def user_image_path(instance, filename):
    folder_path = f'upload/player_{instance.nome}'
    if os.path.exists(folder_path):
        shutil.rmtree(path=folder_path)
    return f'{folder_path}/{filename}'

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
    imagem = models.FileField(upload_to=user_image_path)
    especialidade = models.CharField(max_length=1, choices=opcao_especialidade)
    idade = models.IntegerField()
    sobre = models.TextField()
    status = models.CharField(max_length=1, choices=opcao_status, default='A')
    esta_devendo = models.BooleanField(default=True)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome