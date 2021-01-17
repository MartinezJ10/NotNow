from rest_framework import serializers
from images.models import Images, Category


class ImageSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name")

    class Meta:
        model = Images
        fields = ['id', 'title', 'category', 'alt', 'image', 'created']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = fields
