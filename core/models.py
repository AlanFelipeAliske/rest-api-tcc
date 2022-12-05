from django.db import models
from django.contrib.auth.models import User

class Idiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    idioma_descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.idioma_descricao
        
class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField()
    imagem = models.URLField(max_length=255)
    link = models.URLField(max_length=255)
    idioma = models.ForeignKey(Idiomas, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Posts'        

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
    
    class Meta:
        verbose_name_plural = 'Respostas'
    
    def __str__(self):
        return self.nome


