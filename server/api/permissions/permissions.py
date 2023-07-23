# coding: utf-8
# @author   bovenson
# @email    szhkai@qq.com
# @desc     Django Rest Framework 自定义权限
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserSelfPermission(permissions.BasePermission):
    """如果访问的用户信息不是认证用户则拒绝"""
    message = '只能访问当前用户信息'

    def has_permission(self, request, view):
        # 只有超级用户可以访问列表
        if view.action == 'list':
            self.message = '只有管理员可以访问用户列表'
            return request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id or request.user.is_superuser


class ArticleIsPublicOrAuthor(permissions.BasePermission):
    """文章未公开"""

    def has_object_permission(self, request, view, obj):
        return obj.public or request.user.id == obj.author


class ReadOnlyPermission(BasePermission):
    """只读权限"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ReadOrCreatePermission(BasePermission):
    """读写权限权限"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.method == 'POST'
