from django.db.models import Q
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    CreateAPIView
    )
from rest_framework.filters import (
     SearchFilter,
     OrderingFilter
    )
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )
from ..models import Post
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("z")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__contains=query) |
                Q(description__contains=query)
                ).distinct()
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    #permission_classes = [IsAuthenticated]


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


