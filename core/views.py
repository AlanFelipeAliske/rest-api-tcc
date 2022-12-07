import re
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from collections import UserList
from urllib import response
from django.http import Http404, HttpResponse, JsonResponse
from .serializers import PostsSerializer, RespostasSerializer
from .models import Posts, Respostas
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4


def login_user(request):
    return render(request, 'login.html')
# ---------------------------------------------------------------------------------------------

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/relatorio/')
        else:
            messages.error(request, 'Senha ou usuario invalidos')
        return redirect('/')

# ---------------------------------------------------------------------------------------------

def logout_user(request):
    logout(request)
    return redirect('/')


def inicio(request):
    return render(request, 'inicio.html')


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def relatorio(request):
    var = Respostas.objects.all()
    sql_pais_de_origem = Respostas.objects.raw(
        ''' SELECT MAX (id) as id, 
            pais_de_origem,
            count (*) as contador
            from core_respostas
            group by pais_de_origem 
            order by pais_de_origem '''
    )

    sql_tempo_no_brasil = Respostas.objects.raw(
        ''' SELECT MAX (id) as id, 
            tempo_no_brasil,
            count (*) as contador
            from core_respostas
            group by tempo_no_brasil 
            order by tempo_no_brasil '''
    )

    sql_esta_empregado = Respostas.objects.raw(
        ''' SELECT MAX (id) as id, 
            esta_empregado,
            count (*) as contador
            from core_respostas
            group by esta_empregado 
            order by esta_empregado '''
    )


    response = {
        'vars': var, 
        'sql_pais_de_origems': sql_pais_de_origem, 
        'sql_tempo_no_brasils': sql_tempo_no_brasil,
        'sql_esta_empregados': sql_esta_empregado
    }

    return render(request, 'relatorio.html', response)


def relatoriopdf(request):
    return render(request, 'relatorio.pdf')


class PostLists(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        snippets = Posts.objects.all()
        serializer = PostsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PostDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------

class RespostasLists(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        snippets = Respostas.objects.all()
        serializer = RespostasSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RespostasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RespostasDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Respostas.objects.get(pk=pk)
        except Respostas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RespostasSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RespostasSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ImageDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

