# PART 3 OF TUTORIAL CLASS BASED VIEWS rewriting the views using class-based views
# PART 3 OF TUTORIAL CLASS BASED VIEWS rewriting the views using class-based views
# PART 3 OF TUTORIAL CLASS BASED VIEWS rewriting the views using class-based views

# We can also write our API views using class-based views, rather than function based views as in the previous parts of the tutorial. As we'll see this is a powerful pattern that allows us to reuse common functionality, and helps us keep our code DRY.

# Import necessary modules and classes
# Import the Snippet model from snippets.models
from snippets.models import Snippet
# Import the SnippetSerializer from snippets.serializers
from snippets.serializers import SnippetSerializer
# Import the Http404 exception from django.http
from django.http import Http404
# Import the APIView class from rest_framework.views
from rest_framework.views import APIView
# Import the Response class from rest_framework.response
from rest_framework.response import Response
# Import the status module from rest_framework to access HTTP status codes
from rest_framework import status


# Create a class SnippetList that extends APIView
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    # Define a method for handling GET requests
    def get(self, request, format=None):
        # Retrieve all snippets from the database
        snippets = Snippet.objects.all()
        # Serialize the snippets
        serializer = SnippetSerializer(snippets, many=True)
        # Return the serialized data as a response
        return Response(serializer.data)

    # Define a method for handling POST requests
    def post(self, request, format=None):
        # Create a serializer instance with the request data
        serializer = SnippetSerializer(data=request.data)
        # Check if the serializer data is valid
        if serializer.is_valid():
            # Save the valid serializer data to the database
            serializer.save()
            # Return the serialized data as a response with the status code 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the serializer data is invalid, return the serializer errors as a response
        # with the status code 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# `APIView` is a class provided by the Django REST Framework (DRF) that serves as a base class for creating API views. It is designed to handle HTTP requests and provide appropriate responses.

# By subclassing `APIView`, we can define our own view classes that handle different HTTP methods (e.g., GET, POST, PUT, DELETE) and encapsulate the logic for processing those requests.

# Here are some key features and functionalities provided by `APIView`:

# 1. **Request handling**: `APIView` automatically handles parsing the incoming request and extracting relevant data, such as query parameters, URL parameters, request body, headers, etc. These extracted data can be accessed through the `request` object within the view methods.

# 2. **Response generation**: `APIView` provides convenience methods for generating HTTP responses. For example, the `Response` class allows us to create and return HTTP responses with serialized data, along with appropriate status codes and headers.

# 3. **Method-based request handling**: `APIView` defines separate methods for handling different HTTP methods. For example, `get()` method for handling GET requests, `post()` method for handling POST requests, etc. By overriding these methods in our subclass, we can define our own logic to process the requests.

# 4. **Content negotiation**: `APIView` handles content negotiation, which means it can determine the appropriate response format (e.g., JSON, XML, HTML) based on the client's request. It also supports content negotiation for request data, allowing clients to send data in different formats.

# 5. **Authentication and permissions**: `APIView` provides hooks to handle authentication and permission checks. This allows us to enforce authentication and authorization rules on our API views, ensuring that only authenticated and authorized users can access certain resources or perform specific actions.

# 6. **Error handling**: `APIView` includes error handling mechanisms to handle exceptions and errors that may occur during request processing. It provides default error responses and allows customization of error handling logic.

# In summary, `APIView` is a powerful class provided by the Django REST Framework that simplifies the process of building API views by encapsulating common functionality and providing a consistent interface for handling HTTP requests and generating responses.


# Create a class SnippetDetail that extends APIView
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    # Define a method for retrieving a snippet object by its primary key (pk)
    def get_object(self, pk):
        try:
            # Try to retrieve the snippet with the given primary key
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # If the snippet does not exist, raise the Http404 exception
            raise Http404

    # Define a method for handling GET requests
    def get(self, request, pk, format=None):
        # Get the snippet object based on the provided primary key (pk)
        snippet = self.get_object(pk)
        # Serialize the snippet object
        serializer = SnippetSerializer(snippet)
        # Return the serialized data as a response
        return Response(serializer.data)

    # Define a method for handling PUT requests
    def put(self, request, pk, format=None):
        # Get the snippet object based on the provided primary key (pk)
        snippet = self.get_object(pk)
        # Create a serializer instance with the snippet object and request data
        serializer = SnippetSerializer(snippet, data=request.data)
        # Check if the serializer data is valid
        if serializer.is_valid():
            # Save the valid serializer data to update the snippet object
            serializer.save()
            # Return the serialized data as a response
            return Response(serializer.data)
        # If the serializer data is invalid, return the serializer errors as a response
        # with the status code 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Define a method for handling DELETE requests
    def delete(self, request, pk, format=None):
        # Get the snippet object based on the provided primary key (pk)
        snippet = self.get_object(pk)
        # Delete the snippet object
        snippet.delete()
        # Return a response with status code 204 (No Content)
        return Response(status=status.HTTP_204_NO_CONTENT)
