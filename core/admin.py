from django.contrib import admin 


from core.models import Posts, Respostas, Perguntas, Idiomas

 
class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_titulo', 'post_descricao', 'post_conteudo',)
    list_filter = ('post_titulo', 'post_descricao', 'post_conteudo',)
admin.site.register(Posts, PostsAdmin)


class RespostasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais_de_origem', )
    list_filter = ('nome','pais_de_origem', )
admin.site.register(Respostas, RespostasAdmin)


class PerguntasAdmin(admin.ModelAdmin):
    list_display = ('perguntas_descri',)
    list_filter = ('perguntas_descri',)
admin.site.register(Perguntas, PerguntasAdmin)

class IdiomasAdmin(admin.ModelAdmin):
    list_display = ('idiomas_descri',)
    list_filter = ('idiomas_descri',)
admin.site.register(Idiomas, IdiomasAdmin)


'''


from core.models import Posts, Respostas, Perguntas, Idiomas

class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_titulo', 'post_descricao', 'post_conteudo',)
    list_filter = ('post_titulo', 'post_descricao', 'post_conteudo',)
admin.site.register(Posts, PostsAdmin)

class RespostasAdmin(admin.ModelAdmin):
    list_display = ('respostas_descri',)
    list_filter = ('respostas_descri',)
admin.site.register(Respostas, RespostasAdmin)


class PerguntasAdmin(admin.ModelAdmin):
    list_display = ('perguntas_descri',)
    list_filter = ('perguntas_descri',)
admin.site.register(Perguntas, PerguntasAdmin)

class IdiomasAdmin(admin.ModelAdmin):
    list_display = ('idiomas_descri',)
    list_filter = ('idiomas_descri',)
admin.site.register(Idiomas, IdiomasAdmin)

'''
