from django.db import models
from django.contrib.auth.models import User


"""
class Idiomas(models.Model):
    idiomas_descri = models.CharField(max_length=100)

class Posts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField(max_length=255)
    imagem = models.ImageField()

class Perguntas(models.Model):
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    perguntas_descri = models.CharField(max_length=255)

class Respostas(models.Model):
    pergunta = models.ForeignKey(Perguntas, null=True, on_delete=models.SET_NULL)
    idioma = models.ForeignKey(Idiomas, null=True, on_delete=models.SET_NULL)
    respostas_descri = models.CharField(max_length=255)
"""


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreIdiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    idiomas_descri = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'core_idiomas'

    def __str__(self):
        return self.idiomas_descri

class CorePerguntas(models.Model):
    id = models.BigAutoField(primary_key=True)
    perguntas_descri = models.CharField(max_length=255)
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_perguntas'
    
    def __str__(self):
        return self.perguntas_descri

class CorePosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_titulo = models.CharField(max_length=100)
    post_descricao = models.CharField(max_length=255)
    post_conteudo = models.TextField()
    imagem = models.ImageField()
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_posts'

    def __str__(self):
        return self.post_titulo


class CoreRespostas(models.Model):
    id = models.BigAutoField(primary_key=True)
    respostas_descri = models.CharField(max_length=255)
    idioma = models.ForeignKey(CoreIdiomas, models.DO_NOTHING, blank=True, null=True)
    pergunta = models.ForeignKey(CorePerguntas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_respostas'

    def __str__(self):
        return self.respostas_descri

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



"""     
    def __str__(self):
        return self.respostas_descri
"""
