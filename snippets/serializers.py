# PART_5 OF TUTORIAL Relationships and Hyperlinked APIs
# PART_5 OF TUTORIAL Relationships and Hyperlinked APIs
# PART_5 OF TUTORIAL Relationships and Hyperlinked APIs

# Import the necessary modules
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# Define the SnippetSerializer class, which inherits from serializers.HyperlinkedModelSerializer
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # Add a read-only field 'owner' that represents the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')
    # Add a hyperlink field 'highlight' that represents the URL to the snippet highlight endpoint
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # Define the Meta class to provide metadata for the serializer
    class Meta:
        # Set the model to Snippet
        model = Snippet
        # Define the fields that should be serialized
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


# Define the UserSerializer class, which inherits from serializers.HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Add a hyperlinked related field 'snippets' that represents the related snippets of a user
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    # Define the Meta class to provide metadata for the serializer
    class Meta:
        # Set the model to User
        model = User
        # Define the fields that should be serialized
        fields = ['url', 'id', 'username', 'snippets']

# Notice that we've also added a new 'highlight' field. This field is of the same type as the url field, except that it points to the 'snippet-highlight' url pattern, instead of the 'snippet-detail' url pattern.

# Because we've included format suffixed URLs such as '.json', we also need to indicate on the highlight field that any format suffixed hyperlinks it returns should use the '.html' suffix.

