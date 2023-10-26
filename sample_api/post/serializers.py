from post.models import Post
from rest_framework.serializers import ModelSerializer


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'description']
        
        