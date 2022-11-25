from django.contrib import admin 


from core.models import CorePosts, CoreRespostas, CorePerguntas, CoreIdiomas
 
class CorePostsAdmin(admin.ModelAdmin):
    list_display = ('post_titulo', 'post_descricao', 'post_conteudo',)
    list_filter = ('post_titulo', 'post_descricao', 'post_conteudo',)
admin.site.register(CorePosts, CorePostsAdmin)


class CoreRespostasAdmin(admin.ModelAdmin):
    list_display = ('respostas_descri',)
    list_filter = ('respostas_descri',)
admin.site.register(CoreRespostas, CoreRespostasAdmin)


class CorePerguntasAdmin(admin.ModelAdmin):
    list_display = ('perguntas_descri',)
    list_filter = ('perguntas_descri',)
admin.site.register(CorePerguntas, CorePerguntasAdmin)

class CoreIdiomasAdmin(admin.ModelAdmin):
    list_display = ('idiomas_descri',)
    list_filter = ('idiomas_descri',)
admin.site.register(CoreIdiomas, CoreIdiomasAdmin)


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
