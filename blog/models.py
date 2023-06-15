from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    repo_github = models.URLField(blank=True, null=True)
    pythonanywhere = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    autores = models.ManyToManyField(Autor)
    areas = models.ManyToManyField(Area)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='blog/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo