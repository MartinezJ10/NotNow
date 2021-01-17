from rest_framework import viewsets
from rest_framework import generics

from images.models import Images, Category
from .serializers import ImageSerializer, CategorySerializer


class ImageAPI(viewsets.ModelViewSet):
    queryset = Images.objects.select_related().all()
    serializer_class = ImageSerializer


class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryFilter(generics.ListAPIView):
    queryset = Images.objects.select_related().all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Images.objects.select_related().filter(category_id=self.kwargs.get('pk'))
