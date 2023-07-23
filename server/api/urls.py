from django.urls import path, include
from rest_framework import routers

from api.views.viewsets import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'article/tag', ArticleTagViewSet)
router.register(r'article/category', ArticleCategoryViewSet)
router.register(r'media/images', ImageUploadedViewSet)

urlpatterns = [
    path('user/info/', get_user_info),
    path('upload/image/', ImageUploadedView.as_view()),
    path('auth-token/', AuthTokenView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
