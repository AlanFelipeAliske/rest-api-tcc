from django.db import models
from django.contrib.auth.models import User

class CoreIdiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    idiomas_descri = models.CharField(max_length=100)

class CorePerguntas(models.Model):
    id = models.BigAutoField(primary_key=True)
    perguntas_descri = models.CharField(max_length=255)
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)

class CorePosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField()
    imagem = models.CharField(max_length=255)
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

class CoreRespostas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    pais_de_origem = models.CharField(max_length=255)
    tempo_no_brasil = models.CharField(max_length=255)
    esta_empregado = models.CharField(max_length=255)
    dificuldade_imigrante = models.CharField(max_length=255)
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)
    pergunta = models.ForeignKey(CorePerguntas, models.DO_NOTHING, blank=True, null=True)

