from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from product import views
router = routers.DefaultRouter()
router.register('category',views.CategoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
