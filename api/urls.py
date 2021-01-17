from django.urls import path, include
from rest_framework import routers

from .views import ImageAPI, CategoryAPI, CategoryFilter

router = routers.DefaultRouter()
router.register('images', ImageAPI)
router.register('category', CategoryAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('categoryFilter/<int:pk>/',
         CategoryFilter().as_view(), name='categoryFilter'),
]
