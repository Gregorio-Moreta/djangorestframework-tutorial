from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# CREATING A SERIALIZER CLASS WITH SERIALIZERS.SERIALIZER
# Must specify each field manually, more verbose

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


# CREATING A SERIALIZER CLASS WITH SERIALIZERS.MODELSEIALIZER
# More concise and DRYer, gets information from the model itself rather than having to specify it manually like above for each field
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style'] 

# Create method with self and validated_data as parameters, self is the instance of the class, validated_data is the data that has been validated and is ready for use 
# Snippet.objects.create(**validated_data) creates and returns a new Snippet instance, 
# objects.create is a shortcut for creating and saving an object in a single step, and comes from the serializer's ModelSerializer class,
# **validated_data passes in the validated data as keyword arguments
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
# update method with self, instance, validated_data as parameters, 
# self is a special parameter representing the instance of the class, 
# instance is a parameter name used in the update method of the SnippetSerializer class, it is not a special keyword or reserved name in Python, it just represents an existing snippet instance to be updated which we see in the code below, 
# validated_data.get is the data that has been validated and is ready for use in the update method
# instance.save() saves the updated instance to the database
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




# explain the difference between serializer.ModelSerializer and serializers.serializer

# The difference between `serializer.ModelSerializer` and `serializers.Serializer` lies in their usage and functionality within the Django REST Framework.

# `serializers.Serializer` is the base class provided by the Django REST Framework for creating custom serializers. It is a generic serializer class that allows you to define custom fields and validation logic for your data. You need to manually define all the fields and their serialization/deserialization behavior when subclassing `serializers.Serializer`. It provides a flexible approach for building custom serializers but requires more manual configuration.

# On the other hand, `serializer.ModelSerializer` is a subclass of `serializers.Serializer` that provides additional functionality specifically tailored for working with Django models. It simplifies the process of creating serializers for Django models by automatically generating serializer fields based on the model's fields. You only need to define the model class and optionally specify any additional fields or custom behavior.

# `ModelSerializer` takes care of most of the repetitive tasks, such as generating fields, handling the validation, and implementing the common CRUD operations like `create` and `update`. It automatically maps model fields to corresponding serializer fields and handles serialization and deserialization of model instances.

# By using `ModelSerializer`, you can significantly reduce the amount of code required to define serializers for your Django models. It is a higher-level abstraction that offers convenience and simplicity when working with model-based serialization.

# In summary, `serializers.Serializer` is a generic base class that allows you to define custom serializers, while `serializer.ModelSerializer` is a subclass of `serializers.Serializer` specifically designed for working with Django models and provides automatic field generation and common operations implementation.