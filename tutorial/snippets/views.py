from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.models import Snippet  
from snippets.serializers import SnippetSerializer  
from rest_framework import generics  


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()  
    serializer_class = SnippetSerializer  
    # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()  
    serializer_class = SnippetSerializer  
