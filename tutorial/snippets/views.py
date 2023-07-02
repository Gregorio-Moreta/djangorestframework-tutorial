from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

# This is a Python function that handles HTTP requests for a web application. 
# It defines a view that allows users to list all code snippets or create a new snippet.
# If the request method is GET, it retrieves all code snippets from the database using the Snippet.objects.all() method and serializes them using the SnippetSerializer0 class. 
# It then returns a JSON response containing the serialized data.

# If the request method is POST, it parses the request data using the JSONParser() class and validates it using the SnippetSerializer class. 
# If the data is valid, it saves it to the database using the serializer.save() method and returns a JSON response containing the serialized data and a status code of 201. 
# If the data is not valid, it returns a JSON response containing the validation errors and a status code of 400.
# Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views actually use more sensible behavior than this, but it'll do for our purposes right now.

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

    
# This is a Django view function that handles HTTP requests for a specific code snippet. 
# It takes in a primary key (pk) for the snippet and uses it to retrieve the corresponding Snippet object from the database.

# If the request method is GET, it serializes the Snippet object using the SnippetSerializer and returns it as a JSON response. 
# If the request method is PUT, it parses the request data as JSON, updates the corresponding Snippet object using the SnippetSerializer, and returns the updated object as a JSON response. 
# If the request method is DELETE, it deletes the corresponding Snippet object from the database and returns a 204 No Content response.

# The 
# @csrf_exempt
#  decorator is used to disable CSRF protection for this view, which is useful for testing purposes.

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
