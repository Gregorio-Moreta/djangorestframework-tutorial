# PART_6 Viewsets and Routers
# PART_6 Viewsets and Routers
# PART_6 Viewsets and Routers
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# Import the necessary modules and views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# Define the view functions for the SnippetViewSet and UserViewSet

# snippet_list: handles GET and POST requests for the SnippetViewSet's list and create actions
# This view function is responsible for handling GET requests to retrieve a list of snippets
# It is also responsible for handling POST requests to create a new snippet
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# snippet_detail: handles GET, PUT, PATCH, and DELETE requests for the SnippetViewSet's retrieve, update, partial_update, and destroy actions
# This view function is responsible for handling GET requests to retrieve a specific snippet by its ID
# It is also responsible for handling PUT requests to update the entire snippet, PATCH requests to update specific fields, and DELETE requests to delete the snippet
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# snippet_highlight: handles GET requests for the SnippetViewSet's highlight action with a static HTML renderer
# This view function is responsible for handling GET requests to retrieve the highlighted code of a snippet
# It uses a static HTML renderer to generate the HTML representation of the highlighted code
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list: handles GET requests for the UserViewSet's list action
# This view function is responsible for handling GET requests to retrieve a list of users
user_list = UserViewSet.as_view({
    'get': 'list'
})

# user_detail: handles GET requests for the UserViewSet's retrieve action
# This view function is responsible for handling GET requests to retrieve a specific user by their ID
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


# Define the URL patterns for the API endpoints

# The root endpoint that maps to the api_root view function
# This URL pattern represents the root of the API and maps to the api_root view function
# When a request is made to the root URL, it will be handled by the api_root view function, which provides information about the available endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),

    # Endpoint for the SnippetViewSet's list and create actions
    # This URL pattern maps to the snippet_list view function, which handles GET and POST requests for the SnippetViewSet's list and create actions
    # The URL does not include an ID parameter since it operates on the collection of snippets
    # The 'snippet-list' name is assigned to this URL pattern, which can be used to reverse-resolve the URL in the code
    path('snippets/', snippet_list, name='snippet-list'),

    # Endpoint for the SnippetViewSet's retrieve, update, partial_update, and destroy actions
    # This URL pattern maps to the snippet_detail view function, which handles GET, PUT, PATCH, and DELETE requests for the SnippetViewSet's retrieve, update, partial_update, and destroy actions
    # The '<int:pk>/' part in the URL represents the ID parameter of the snippet to operate on
    # The 'snippet-detail' name is assigned to this URL pattern, which can be used to reverse-resolve the URL in the code
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),

    # Endpoint for the SnippetViewSet's highlight action
    # This URL pattern maps to the snippet_highlight view function, which handles GET requests for the SnippetViewSet's highlight action
    # The '<int:pk>/' part in the URL represents the ID parameter of the snippet to operate on
    # The 'snippet-highlight' name is assigned to this URL pattern, which can be used to reverse-resolve the URL in the code
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),

    # Endpoint for the UserViewSet's list action
    # This URL pattern maps to the user_list view function, which handles GET requests for the UserViewSet's list action
    # The URL does not include an ID parameter since it operates on the collection of users
    # The 'user-list' name is assigned to this URL pattern, which can be used to reverse-resolve the URL in the code
    path('users/', user_list, name='user-list'),

    # Endpoint for the UserViewSet's retrieve action
    # This URL pattern maps to the user_detail view function, which handles GET requests for the UserViewSet's retrieve action
    # The '<int:pk>/' part in the URL represents the ID parameter of the user to operate on
    # The 'user-detail' name is assigned to this URL pattern, which can be used to reverse-resolve the URL in the code
    path('users/<int:pk>/', user_detail, name='user-detail')
])
