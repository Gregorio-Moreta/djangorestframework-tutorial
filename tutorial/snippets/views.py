# PART_6 Viewsets and Routers
# PART_6 Viewsets and Routers
# PART_6 Viewsets and Routers

from rest_framework.decorators import action
from rest_framework import viewsets

# Import necessary modules
from snippets.serializers import UserSerializer
from snippets.models import Snippet  
from snippets.serializers import SnippetSerializer  
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import renderers


# Here we've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations. We're still setting the queryset and serializer_class attributes exactly as we did when we were using regular views, but we no longer need to provide the same information to two separate classes.

# Define the UserViewSet class, which inherits from viewsets.ReadOnlyModelViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    # Set the queryset to retrieve all User objects
    queryset = User.objects.all()
    # Set the serializer class to be used for User objects
    serializer_class = UserSerializer

# The UserViewSet class is a subclass of viewsets.ReadOnlyModelViewSet, which provides default implementations for read-only actions (list and retrieve) on a model.

# By setting the queryset attribute to User.objects.all(), all User objects in the database will be retrieved for this viewset.

# The serializer_class attribute is set to UserSerializer, which specifies the serializer class to be used for serializing User objects.

# Please note that the code assumes that you have imported the necessary modules (User, viewsets, etc.) and have defined the UserSerializer class. Additionally, make sure to include the UserViewSet in your URL configuration to make it accessible through the API.




# This time we've used the ModelViewSet class in order to get the complete set of default read and write operations.

# Notice that we've also used the @action decorator to create a custom action, named highlight. This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.

# Custom actions which use the @action decorator will respond to GET requests by default. We can use the methods argument if we wanted an action that responded to POST requests.

# The URLs for custom actions by default depend on the method name itself. If you want to change the way url should be constructed, you can include url_path as a decorator keyword argument.

# Define the SnippetViewSet class, which inherits from viewsets.ModelViewSet
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions.

    Additionally, we also provide an extra `highlight` action.
    """
    # Set the queryset to retrieve all Snippet objects
    queryset = Snippet.objects.all()
    # Set the serializer class to be used for Snippet objects
    serializer_class = SnippetSerializer
    # Set the permission classes to control access permissions for Snippet views
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Define an additional action 'highlight' that responds to GET requests with a static HTML renderer
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        # Retrieve the specific Snippet object
        snippet = self.get_object()
        # Return the highlighted code of the Snippet as the response
        return Response(snippet.highlighted)

    # Override the perform_create() method to associate the Snippet owner with the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

