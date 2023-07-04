# django.db.models is imported from the Django framework, which provides the base class Model for creating models.
from django.db import models
# pygments.lexers.get_all_lexers is imported from the Pygments library, which provides a function to retrieve a list of available lexers (syntax highlighters).
from pygments.lexers import get_all_lexers
# pygments.styles.get_all_styles is imported from the Pygments library as well, which provides a function to retrieve a list of available styles for syntax highlighting.
from pygments.styles import get_all_styles

# Create your models here.
# This line retrieves a list of available lexers (syntax highlighters) using the get_all_lexers() function from Pygments. 
# It then filters out any empty lexers by using a list comprehension. 
# The resulting list, LEXERS, contains only the non-empty lexers.
LEXERS = [item for item in get_all_lexers() if item[1]]

# This line generates language choices for the language field of the Snippet model. 
# It creates a sorted list of tuples using a list comprehension. 
# Each tuple contains the language name (obtained from item[1][0]) and the lexer short name (obtained from item[0]) from the LEXERS list. 
# The resulting list, LANGUAGE_CHOICES, represents the available choices for the language field.
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

# This line generates style choices for the style field of the Snippet model. It creates a sorted list of tuples using a list comprehension. 
# Each tuple contains the style name (obtained from item) as both the display value and the stored value. 
# The resulting list, STYLE_CHOICES, represents the available choices for the style field.
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


    # class Snippet(models.Model): declares a class named Snippet that inherits from models.Model, which is the base class for all Django models.
class Snippet(models.Model):
    # created = models.DateTimeField(auto_now_add=True) defines a field named created of type DateTimeField. 
    # The auto_now_add=True parameter automatically sets the field's value to the current date and time when a new Snippet instance is created.
    created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='') defines a field named title of type CharField. 
    # It has a maximum length of 100 characters, allows blank values, and has a default value of an empty string.
    title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField() defines a field named code of type TextField. 
    # It stores large text content such as code snippets.
    code = models.TextField()
    # linenos = models.BooleanField(default=False) defines a field named linenos of type BooleanField. 
    # It represents whether line numbers should be displayed for the code snippet and has a default value of False.
    linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100) defines a field named language of type CharField. 
    # It uses the choices parameter to restrict the available choices to the LANGUAGE_CHOICES defined earlier. 
    # The default value is set to 'python', and the maximum length is 100 characters.
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100) defines a field named style of type CharField. 
    # It uses the choices parameter to restrict the available choices to the STYLE_CHOICES defined earlier. 
    # The default value is set to 'friendly', and the maximum length is 100 characters.
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    # class Meta: defines a nested class within the Snippet class called Meta. It is used to provide metadata and configurations for the model.
    class Meta:
        # ordering = ['created'] specifies that the Snippet instances should be ordered based on the created field. 
        # The 'created' string represents the field name, and the ordering is set to ascending order.
        ordering = ['created']

# In summary, the provided code defines a Snippet model with various fields representing attributes of a code snippet. 
# It also specifies metadata such as ordering for instances of the model.