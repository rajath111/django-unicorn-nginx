"""
URL configuration for sample_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf.urls.static import static
from django.conf import settings

@api_view(['get'])
def test_api(request):
    return Response('Running Successfully!!!', status=status.HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('test/', view=test_api, name='test-api'),
] + static(settings.STATIC_URL, document_path=settings.STATIC_ROOT)