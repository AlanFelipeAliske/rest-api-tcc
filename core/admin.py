
from django.contrib import admin
from core.models import CorePosts, CoreRespostas, CorePerguntas

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


