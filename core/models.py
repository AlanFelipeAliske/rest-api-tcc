from django.db import models
from django.contrib.auth.models import User

class Idiomas(models.Model):
    idiomas_descri = models.CharField(max_length=100)


class Posts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField(max_length=255)


class Perguntas(models.Model):
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    perguntas_descri = models.CharField(max_length=255)


class Respostas(models.Model):
    pergunta = models.ForeignKey(Perguntas, null=True, on_delete=models.SET_NULL)
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    respostas_descri = models.CharField(max_length=255)






'''     
    def __str__(self):
        return self.respostas_descri
'''