from collections import OrderedDict

from rest_framework import serializers
from django.contrib.auth.models import Group
from rest_framework.fields import SkipField
from rest_framework_recursive.fields import RecursiveField

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ArticleCategorySerializer(serializers.ModelSerializer):
    """文章分类"""
    children = RecursiveField(many=True)

    class Meta:
        model = ArticleCategory
        fields = '__all__'

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive data types.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                    # Do not serialize empty lists
                    continue
                ret[field.field_name] = represenation
        return ret


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """文章"""

    class Meta:
        model = Article
        fields = '__all__'

    def run_validation(self, data=serializers.empty):
        """验证数据"""
        # 设置用户
        data['author'] = self.context['request'].user.id
        # 标签
        if 'tags' in data:
            # 标签判断; 如果不存在则新建
            for tag in data['tags']:
                ArticleTag.objects.get_or_create(name=tag)
        return super(ArticleSerializer, self).run_validation(data)

    def create(self, validated_data):
        """新建文章"""
        tags = validated_data.pop('tags')
        instance = Article.objects.create(**validated_data)
        instance.tags.set(tags)
        instance.save()
        return instance


class ImageUploadedSerializer(serializers.ModelSerializer):

    file = serializers.ImageField(use_url=True)

    class Meta:
        model = ImageUploaded
        fields = ['id', 'file', 'create_datetime']
