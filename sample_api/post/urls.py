from django.urls import path
from post.views import PostApiView

urlpatterns = [
    path('', view=PostApiView.as_view(), name='post'),
]