# PART 1 OF TUTORIAL SERIALIZERS
# PART 1 OF TUTORIAL SERIALIZERS
# PART 1 OF TUTORIAL SERIALIZERS

from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# Create your views here.

# This is a Python function that handles HTTP requests for a web application. 
# It defines a view that allows users to list all code snippets or create a new snippet.
# If the request method is GET, it retrieves all code snippets from the database using the Snippet.objects.all() method and serializes them using the SnippetSerializer0 class. 
# It then returns a JSON response containing the serialized data.

# If the request method is POST, it parses the request data using the JSONParser() class and validates it using the SnippetSerializer class. 
# If the data is valid, it saves it to the database using the serializer.save() method and returns a JSON response containing the serialized data and a status code of 201. 
# If the data is not valid, it returns a JSON response containing the validation errors and a status code of 400.
# Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views actually use more sensible behavior than this, but it'll do for our purposes right now.

# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    

    
# This is a Django view function that handles HTTP requests for a specific code snippet. 
# It takes in a primary key (pk) for the snippet and uses it to retrieve the corresponding Snippet object from the database.

# If the request method is GET, it serializes the Snippet object using the SnippetSerializer and returns it as a JSON response. 
# If the request method is PUT, it parses the request data as JSON, updates the corresponding Snippet object using the SnippetSerializer, and returns the updated object as a JSON response. 
# If the request method is DELETE, it deletes the corresponding Snippet object from the database and returns a 204 No Content response.

# The 
# @csrf_exempt
#  decorator is used to disable CSRF protection for this view, which is useful for testing purposes.

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)




# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# Import necessary modules/classes from Django REST framework

# Request objects
# REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.

# Response objects
# REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.

# Status codes
# Using numeric HTTP status codes in your views doesn't always make for obvious reading, and it's easy to not notice if you get an error code wrong. REST framework provides more explicit identifiers for each status code, such as HTTP_400_BAD_REQUEST in the status module. It's a good idea to use these throughout rather than using numeric identifiers.

# Wrapping API views
# REST framework provides two wrappers you can use to write API views.
# The @api_view decorator for working with function based views.
# The APIView class for working with class-based views.
# These wrappers provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.

# The wrappers also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.

# Notice that we're no longer explicitly tying our requests or responses to a given content type. request.data can handle incoming json requests, but it can also handle other formats. Similarly we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us.

# Adding optional format suffixes to our URLs
# Start by adding a format keyword argument to both of the views, like so.
# def snippet_list(request, format=None):
# def snippet_detail(request, pk, format=None):
# FORMAT SUFFIXES ARE OPTIONAL, DON'T FEEL COMPELLED TO USE THIS FEATURE IF YOUR API DOESN'T NEED IT.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Define a view function that handles GET and POST requests
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    # If the request method is GET
    if request.method == 'GET':
        # Retrieve all Snippet objects from the database
        snippets = Snippet.objects.all()
        # Serialize the snippets data
        serializer = SnippetSerializer(snippets, many=True)
        # Return the serialized data in the response
        # JsonResponse is a subclass of HttpResponse that can be used to output JSON data, I replaced Response with JsonResponse so that the data is displayed on the page rather then default to a template, and it works fine.
        return JsonResponse(serializer.data, safe=False)

    # If the request method is POST
    elif request.method == 'POST':
        # Create a new SnippetSerializer instance with request data
        serializer = SnippetSerializer(data=request.data)
        # Check if the serializer data is valid
        if serializer.is_valid():
            # Save the serializer data (create a new Snippet object)
            serializer.save()
            # Return the serialized data in the response with HTTP 201 status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the serializer data is not valid, return the errors in the response with HTTP 400 status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define a view function that handles GET, PUT, and DELETE requests
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        # Try to retrieve a Snippet object with the specified primary key (pk)
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        # If no Snippet object is found, return HTTP 404 status code
        return Response(status=status.HTTP_404_NOT_FOUND)

    # If the request method is GET
    if request.method == 'GET':
        # Serialize the snippet data
        serializer = SnippetSerializer(snippet)
        # Return the serialized data in the response
        return Response(serializer.data)

    # If the request method is PUT
    elif request.method == 'PUT':
        # Update the existing snippet object with request data
        serializer = SnippetSerializer(snippet, data=request.data)
        # Check if the serializer data is valid
        if serializer.is_valid():
            # Save the serializer data (update the Snippet object)
            serializer.save()
            # Return the serialized data in the response
            return Response(serializer.data)
        # If the serializer data is not valid, return the errors in the response with HTTP 400 status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # If the request method is DELETE
    elif request.method == 'DELETE':
        # Delete the snippet object
        snippet.delete()
        # Return HTTP 204 status code indicating successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)

# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS

# Part 3 is continued in the snippets folder in the views.py file, I renamed this one to views-Parts-1-2.py to avoid confusion and to make it easier to find the code for part 3, check that out, this code won't be used now.