# PART 3 OF TUTORIAL CLASS BASED VIEWS Using generic class-based views
# PART 3 OF TUTORIAL CLASS BASED VIEWS Using generic class-based views
# PART 3 OF TUTORIAL CLASS BASED VIEWS Using generic class-based views

# Using generic class-based views
# Using the mixin classes we've rewritten the views to use slightly less code than before, but we can go one step further. REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.

# Importing the necessary modules and classes
# Importing the Snippet model from the snippets.models module
from snippets.models import Snippet  
# Importing the SnippetSerializer class from the snippets.serializers module
from snippets.serializers import SnippetSerializer  
# Importing the generics module from the rest_framework package
from rest_framework import generics  

# Defining a class called SnippetList that inherits from generics.ListCreateAPIView
class SnippetList(generics.ListCreateAPIView):
    # A queryset is created by retrieving all Snippet objects from the database
    queryset = Snippet.objects.all()  
    # Assigning the SnippetSerializer class to the serializer_class attribute
    serializer_class = SnippetSerializer  

# Defining a class called SnippetDetail that inherits from generics.RetrieveUpdateDestroyAPIView
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # A queryset is created by retrieving all Snippet objects from the database
    queryset = Snippet.objects.all()  
    # Assigning the SnippetSerializer class to the serializer_class attribute
    serializer_class = SnippetSerializer  

# Wow, that's pretty concise. We've gotten a huge amount for free, and our code looks like good, clean, idiomatic Django.

# Next we'll move onto part 4 of the tutorial, where we'll take a look at how we can deal with authentication and permissions for our API.