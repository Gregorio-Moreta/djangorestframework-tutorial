from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.models import Snippet  
from snippets.serializers import SnippetSerializer  
from rest_framework import generics  
# This code imports the permissions module from the Django REST Framework.
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()  
    serializer_class = SnippetSerializer  
    # permission_classes are used to specify the permissions that will be enforced on the view.
    # Assign the IsAuthenticatedOrReadOnly permission class to the permission_classes attribute

    # Pseudocode explanation:
    # This code imports the permissions module from the Django REST Framework.
    # It then assigns the IsAuthenticatedOrReadOnly permission class to the permission_classes attribute.
    # This permission class allows authenticated users to have full access (read and write) to the resource,
    # while unauthenticated users are only allowed read access (GET requests) and denied write access (POST, PUT, DELETE requests).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()  
    serializer_class = SnippetSerializer  
    # permission_classes are used to specify the permissions that will be enforced on the view.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
