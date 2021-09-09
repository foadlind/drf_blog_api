from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
