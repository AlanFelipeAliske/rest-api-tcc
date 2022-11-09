
from rest_framework import serializers
from .models import Posts, Perguntas, Respostas

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'

class PerguntasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Perguntas
        fields = '__all__'

class RespostasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Respostas
        fields = '__all__'
