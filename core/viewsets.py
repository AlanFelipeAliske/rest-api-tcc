from core.serializers import PostsSerializer
from rest_framework import viewsets, permissions
from core.models import Posts


class PostsViewSet(viewsets.ModelViewSet):
  
  permission_classes = [permissions.IsAuthenticated]

  queryset = Posts.objects.all()
  serializer_class = PostsSerializer