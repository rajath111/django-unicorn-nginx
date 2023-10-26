from rest_framework.generics import GenericAPIView
from post.serializers import PostCreateSerializer
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from post.models import Post
from rest_framework import status

class PostApiView(GenericAPIView):

    authentication_classes = []
    serializer_class = PostCreateSerializer

    def get(self, request: HttpRequest) -> Response:
        return Response([self.serializer_class(post).data for post in Post.objects.all()], status=status.HTTP_200_OK)

    def post(self, request: HttpRequest) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)