from django.db import models
from django.contrib.auth.models import User

class Idiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    idiomas_descri = models.CharField(max_length=100)

    def __str__(self):
        return self.idiomas_descri
        
class Perguntas(models.Model):
    id = models.BigAutoField(primary_key=True)
    perguntas_descri = models.CharField(max_length=255)
    idioma = models.ForeignKey(Idiomas, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.perguntas_descri

class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField()
    imagem = models.CharField(max_length=255)
    idioma = models.ForeignKey(Idiomas, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return self.post_titulo

class Respostas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    pais_de_origem = models.CharField(max_length=255)
    tempo_no_brasil = models.CharField(max_length=255)
    esta_empregado = models.CharField(max_length=255)
    dificuldade_imigrante = models.CharField(max_length=255)
    idioma = models.ForeignKey(Idiomas, models.DO_NOTHING, blank=True, null=True)
    pergunta = models.ForeignKey(Perguntas, models.DO_NOTHING, blank=True, null=True)
    



