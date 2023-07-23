# coding: utf-8
# @author   bovenson
# @email    szhkai@qq.com
# @desc     Django Rest Framework Viewsets

from django.forms.models import model_to_dict
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from api.core.pagination import ArticleListPagination
from api.permissions.permissions import ReadOnlyPermission, ReadOrCreatePermission
from api.serializers.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    http_method_names = ['get']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AuthTokenView(ObtainAuthToken):
    """获取token 并返回用户信息"""

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': model_to_dict(user)
        })


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated | ReadOnlyPermission])
def get_user_info(request):
    """获取认证用户信息"""
    return Response(model_to_dict(request.user))


class ArticleViewSet(viewsets.ModelViewSet):
    """文章ViewSet"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination

    permission_classes = [ReadOnlyPermission | IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def summary(self, request):
        """获取带有限定字符简介的列表"""
        articles = Article.objects.filter(public=True)
        for article in articles:
            article.content = article.content[:120]

        # 分页
        page = self.paginate_queryset(articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(articles, many=True)
            return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def filter(self, request: Request):
        if 'tag' in request.query_params:
            queryset = Article.objects.filter(public=True, tags__in=[request.query_params.get('tag')])
        elif 'cate' in request.query_params:
            queryset = Article.objects.filter(public=True, category__name__in=[request.query_params.get('cate')])
        else:
            queryset = Article.objects.filter(public=True)

        # 分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class ArticleTagViewSet(viewsets.ModelViewSet):
    """文章标签列表"""
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    permission_classes = [IsAuthenticated | ReadOnlyPermission]


class ArticleCategoryViewSet(viewsets.ModelViewSet):
    """文章分类列表"""
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    permission_classes = [IsAuthenticated | ReadOnlyPermission]

    @action(methods=['GET'], detail=False)
    def tree(self, request):
        """返回文章分类树"""
        prefetch = ArticleCategory.objects.all().prefetch_related()
        childs = list(map(lambda x: x.get('children'), prefetch.filter(children__isnull=False).values('children')))
        query = prefetch.exclude(pk__in=childs)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)


class ImageUploadedViewSet(viewsets.ModelViewSet):
    """图片"""
    queryset = ImageUploaded.objects.all()
    serializer_class = ImageUploadedSerializer
    permission_classes = [IsAuthenticated | ReadOnlyPermission]


class ImageUploadedView(views.APIView):
    """图片上传"""

    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated | ReadOrCreatePermission]

    def post(self, request: Request):
        request.FILES['file'] = request.FILES['editormd-image-file']
        request.data['file'] = request.data['editormd-image-file']
        request.accepted_renderer.format = 'json'
        serializer = ImageUploadedSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({
                'success': 1,
                'message': '图片上传成功',
                'url': request.build_absolute_uri(serializer.data.get('file')),
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
