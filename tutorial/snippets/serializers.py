# PART 4 OF TUTORIAL Authentication & Permissions
# PART 4 OF TUTORIAL Authentication & Permissions
# PART 4 OF TUTORIAL Authentication & Permissions

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    # Now that snippets are associated with the user that created them, let's update our SnippetSerializer to reflect that. Add the following field to the serializer definition in serializers.py:
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        # Note: Make sure you also add 'owner', to the list of fields in the inner Meta class.
        fields = ['owner', 'id', 'title', 'code', 'linenos', 'language', 'style'] 
        # This field is doing something quite interesting. The source argument controls which attribute is used to populate a field, and can point at any attribute on the serialized instance. It can also take the dotted notation shown above, in which case it will traverse the given attributes, in a similar way as it is used with Django's template language.

        # The field we've added is the untyped ReadOnlyField class, in contrast to the other typed fields, such as CharField, BooleanField etc... The untyped ReadOnlyField is always read-only, and will be used for serialized representations, but will not be used for updating model instances when they are deserialized. We could have also used CharField(read_only=True) here.

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
# Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.

# We'll also add a couple of views to views.py. 
# We'd like to just use read-only views for the user representations, so we'll use the ListAPIView and RetrieveAPIView generic class-based views.


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
