from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import BlogPost
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class PostApiList(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    """
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        return super(PostApiList, self).get_permissions()

    def create(self, request, pk=None):
        if request.user.pk == pk:
            post = PostSerializer(data = request.data)
            post.is_valid(raise_exception=True)
            post.save()
        else:
            return Response('Failure {request.user.pk} does not have permissions', status=400)
    """
    def retrieve(self, request, pk=None):
        posts = BlogPost.objects.filter(author = pk)
        post_response = [PostSerializer(x).data for x in posts ]
        return Response(post_response)