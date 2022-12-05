from django.contrib import admin 


from core.models import Posts, Respostas, Idiomas

class IdiomasAdmin(admin.ModelAdmin):
    list_display = ('idioma_descricao',)
admin.site.register(Idiomas, IdiomasAdmin)
 
class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_titulo', 'post_descricao', 'post_conteudo',)
admin.site.register(Posts, PostsAdmin)

class RespostasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais_de_origem', 'tempo_no_brasil', 'esta_empregado', 'dificuldade_imigrante', )
admin.site.register(Respostas, RespostasAdmin)
