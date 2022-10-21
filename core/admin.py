from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_titulo', 'post_descricao', 'post_conteudo')
    list_filter = ('post_titulo', 'post_descricao', 'post_conteudo')
admin.site.register(Posts, PostsAdmin)






