# Djangorestframework-tutorial
## Build the official tutorial app

There are 6 parts in total listed at the bottom of this repo in the [References](#references), going from default django features to replacing them with djangorestframework specific tools.

I won't write everything over from the tutorials, but I have added significant comments and intend to write each of the 6 tutorial parts with comments.

Also, I haven't installed the http client in python, I'm just using postman. The shell commands given are fully functional as well, so use those along the way.

### Setting up environment
You can use any environment you prefer so long as you know how to use them properly. 
For some of you, pip may cause problems, you can use homebrew to install these if you need to as well.
Options include:
- venv ( this is what the tutorial uses )
- pipenv
- mkvirtualenv ( we used this one in class )

#### venv
```
python3 -m venv env
source env/bin/activate
```
#### pipenv
- https://pipenv-fork.readthedocs.io/en/latest/basics.html
- https://formulae.brew.sh/formula/pipenv
- https://medium.com/geekculture/setting-up-python-environment-in-macos-using-pyenv-and-pipenv-116293da8e72
```
Note, if you install this you will generate a Pipfile
This works differently from the others
You don't need pipfreeze > requirements.txt anymore
All you need to do is pipenv install < package name >
This will automatically install it to your project environment
```

#### mkvirtualenv
- https://virtualenvwrapper.readthedocs.io/en/latest/install.html
```
Install
pip install virtualenvwrapper
Example usage:

Create a virtual environment:
mkvirtualenv myenv ( name your 'myenv' after your project; it's easier to keep track of )

E.G 
mkvirtualenv djangorestframework-tutorial

Activate the virtual environment:
workon myenv

Deactivate the virtual environment:
deactivate

If you can't create a virtual environment, make sure path is correct
code ~/.zshrc

inside your ~./zshrc folder you should include these 

export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh

then run source ~/.zshrc to save your changes in the ~/.zshrc file
If those values don't work, run these commands and replace the values accordingly

which python3
which virtualenv
which virtualenvwrapper.sh

Then run source ~/.zshrc to save your changes in the ~/.zshrc file again

Now you should be able to mkvirtualenv djangorestframework-tutorial
```
All of these are viable options, but they each operate slightly differently.
There are other env options still, however you shouldn't need anymore than these. 
If one gives you too many issues you can simply try another.

### Installation
#### Part_1 Serialization
Follow along here
- https://www.django-rest-framework.org/tutorial/1-serialization/

I even left the code that we eventually replaced. 
I added comments to it so as to add context about why it was replaced, from pure django to djangorestframework.

#### Part_2 Requests and Responses
- https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
Not much has changed except a couple additions
```
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
```
Some of these are new and explained here, api_view, Response, status

#### Part_3 Class Based Views
- https://www.django-rest-framework.org/tutorial/3-class-based-views/
If you want to test the different types of ways you can build your views, just rename whatever file you want to be as views 

example 
```
views-Part-3-using-class-based-views.py
or
views-Part-3-using-mixins.py

remamed to 

views.py

You can rename the other file you're not using so django doesn't get confused

Remember to restart your database when you do this so the changes are run
```

```
APIView
from rest_framework.views import APIView

or

gnerics view
from rest_framework import generics  

```

This way you should be able to learn about the different approaches available. For now I will leave the generic class-based views as my views.py, unless the tutorial changes it down the line.

#### Part_4 Authentication and Permissions
- https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
```
snippets/models.py
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

tutorial/urls.py 
from django.views.generic import RedirectView

snippets/permissions.py
from rest_framework import permissions

snippets/serializer.py
from django.contrib.auth.models import User


```
- Check out the Part_4 summary section
There were modifications to the views (adding permissions), models(adding owner field and method), urls in both the tutorial project and snippets app, the addition of the permissions file.

Now we should be able to use rest_framework (which is in the settings.py in the INSTALLED_APPS list), to have athentication and authorization based on the default authentication classes and permissions.

You can do this many different ways, this is just the built in way
- https://www.django-rest-framework.org/api-guide/authentication/

I have seen knox work well for most that try and implement it
- https://github.com/James1345/django-rest-knox

#### DATABASE
When we update our model, be sure to delete the db.sqlite3 file, re-run migration commands.
```
When that's all done we'll need to update our database tables. 
Normally we'd create a database migration in order to do that, but for the purposes of this tutorial, let's just delete the database and start again.

rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate
You might also want to create a few different users, to use for testing the API. The quickest way to do this will be with the createsuperuser command.

python manage.py createsuperuser
```

#### Part_5 Relationships and Hyperlinked APIs
- https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
snippets/views.py
```
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
```

#### Part_6 Viewsets and Routers
- https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/




### Summary
#### Part_1 Serialization

At the end of part 1, you should be able to perform full CRUD functionality. 

There is still a lot of djangorestframework specific modifications required to make it a RESTful API, but those features are explained in the later tutorials.

I have created models, serializers, urls, views, a project called tutorial, and an app called snippets. So far we are using the default sqlite3 database.

I added the snippets app to the settings.py for my tutorial project inside of the install_apps list.

I ran makemigrations and migrate so my models should be synched with the database as well.

If I missed something I'll add it later. Please make an issue if you want to bring something to my attention. Thank you, kindly!

#### Part_2 Requests and Responses
Covered these topics in the snippets/views.py and snippets/urls.py
- Responses
- Requests
- Status Codes
- Wrapping API view
- Adding optional format suffixes to URLs 

Checkout the docs for further details about how these features work and refer to the screenshots below.
Note that I also included comments explaining much of this in the files on this branch and commit so check those out.

![alt text](./Images/Part-2/Screen%20Shot%202023-07-02%20at%208.21.33%20PM.png)
![alt text](./Images/Part-2/Screen%20Shot%202023-07-02%20at%208.23.01%20PM.png)

#### Part_3 Class Based Views
I made new views files for this part_3 so there is one for rewriting our API using 
- class-based views
- mixins
- generic class-based views

The code is more concise and uses the APIView class as explained in the new views files comments. Essentially it handles a lot of scenarios for you out of the box so you don't need to manually configure everything in your views like before. It will allow us to build features more quickly.

#### Part_4 Authentication and Permissions
- Adding information to our model
```
Add the following two fields to the Snippet model in snippets/models.py.
One of those fields will be used to represent the user who created the code snippet. 
The other field will be used to store the highlighted HTML representation of the code.


owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()

Updated modelclass Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ['created']

```

- Adding endpoints for our User models 
```
serializers.py
Now that we've got some users to work with, we'd better add representations of those users to our API. 
Creating a new serializer is easy. In serializers.py add:

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
```
- Association Snippets with Users
```
Right now, if we created a code snippet, there'd be no way of associating the user that created the snippet, with the snippet instance. The user isn't sent as part of the serialized representation, but is instead a property of the incoming request.

The way we deal with that is by overriding a .perform_create() method on our snippet views, that allows us to modify how the instance save is managed, and handle any information that is implicit in the incoming request or requested URL.

On the SnippetList view class, add the following method:

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
```
- Updating our serializer
```
Now that snippets are associated with the user that created them, let's update our SnippetSerializer to reflect that. Add the following field to the serializer definition in serializers.py:

owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        # Note: Make sure you also add 'owner', to the list of fields in the inner Meta class.  
        fields = ['owner', 'id', 'title', 'code', 'linenos', 'language', 'style'] 


```
- Adding required permissions to views
```
Now that code snippets are associated with users, we want to make sure that only authenticated users are able to create, update and delete code snippets.

REST framework includes a number of permission classes that we can use to restrict who can access a given view. In this case the one we're looking for is IsAuthenticatedOrReadOnly, which will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access.

First add the following import in the views module

    from rest_framework import 
    
Then, add the following property to both the SnippetList and SnippetDetail view classes.

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```
- Adding login to the Browsable API
```
tutorial/urls.py
If you open a browser and navigate to the browsable API at the moment, you'll find that you're no longer able to create new code snippets. 
In order to do so we'd need to be able to login as a user.

We can add a login view for use with the browsable API, by editing the URLconf in our project-level urls.py file.

Add the following import at the top of the file:

from django.urls import path, include
And, at the end of the file, add a pattern to include the login and logout views for the browsable API.

    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]
The 'api-auth/' part of pattern can actually be whatever URL you want to use.

Now if you open up the browser again and refresh the page you'll see a 'Login' link in the top right of the page. 
If you log in as one of the users you created earlier, you'll be able to create code snippets again.

Once you've created a few code snippets, navigate to the '/users/' endpoint, and notice that the representation includes a list of the snippet ids that are associated with each user, in each user's 'snippets' field.

I added a redirect in the tutorial/urls.py file because by default django doesn't redirect you to your route to the model. 
It would direct you to /accounts/profile, so I made the redirect to 'snippets'. 
After a user logs in from the 'api-auth' page, they are sent to the 'snippets' page and now have access to the protected routes/ views we added.

Check the Application tab, the cookies section and look for the token, if you have a token odds are you are authenticated for other routes
```
- Object level permissions
create a new file
snippets/permissions.py
```
Really we'd like all code snippets to be visible to anyone, but also make sure that only the user that created a code snippet is able to update or delete it.

To do that we're going to need to create a custom permission.

In the snippets app, create a new file, permissions.py

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
Now we can add that custom permission to our snippet instance endpoint, by editing the permission_classes property on the SnippetDetail view class:

permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
Make sure to also import the IsOwnerOrReadOnly class.

from snippets.permissions import IsOwnerOrReadOnly
Now, if you open a browser again, you find that the 'DELETE' and 'PUT' actions only appear on a snippet instance endpoint if you're logged in as the same user that created the code snippet.

```
![alt text](./Images/Part-4/Screen%20Shot%202023-07-04%20at%205.12.31%20AM.png)

Notice that I am signed in as user1 and now have access to the PUT and DELETE buttons/ options which is authorized through the permissions.py file.

![alt text](./Images/Part-4/Screen%20Shot%202023-07-04%20at%205.15.06%20AM.png)

This is the view when you are signed in as user1 but view another user's Snippets. The option to DELETE or PUT is now unavailable because the Snippet belongs to anoher user.
- Authenticating with the API
```
Because we now have a set of permissions on the API, we need to authenticate our requests to it if we want to edit any snippets. We haven't set up any authentication classes, so the defaults are currently applied, which are SessionAuthentication and BasicAuthentication.

When we interact with the API through the web browser, we can login, and the browser session will then provide the required authentication for the requests.

If we're interacting with the API programmatically we need to explicitly provide the authentication credentials on each request.

If we try to create a snippet without authenticating, we'll get an error:

http POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
    "detail": "Authentication credentials were not provided."
}
We can make a successful request by including the username and password of one of the users we created earlier.

http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(789)"

{
    "id": 1,
    "owner": "admin",
    "title": "foo",
    "code": "print(789)",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```
![alt text](./Images/Part-4/Screen%20Shot%202023-07-04%20at%205.35.58%20AM.png)
- Summary

We've now got a fairly fine-grained set of permissions on our Web API, and end points for users of the system and for the code snippets that they have created.

In part 5 of the tutorial we'll look at how we can tie everything together by creating an HTML endpoint for our highlighted snippets, and improve the cohesion of our API by using hyperlinking for the relationships within the system.

#### Part_5 Relationships and Hyperlinked APIs
- Creating an endpoint for the root of our API
```
Right now we have endpoints for 'snippets' and 'users', but we don't have a single entry point to our API. To create one, we'll use a regular function-based view and the @api_view decorator we introduced earlier. In your snippets/views.py add:

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
Two things should be noticed here. First, we're using REST framework's reverse function in order to return fully-qualified URLs; second, URL patterns are identified by convenience names that we will declare later on in our snippets/urls.py.
```
- Creating an endpoint for the highlighted snippets
```
The other obvious thing that's still missing from our pastebin API is the code highlighting endpoints.

Unlike all our other API endpoints, we don't want to use JSON, but instead just present an HTML representation. There are two styles of HTML renderer provided by REST framework, one for dealing with HTML rendered using templates, the other for dealing with pre-rendered HTML. The second renderer is the one we'd like to use for this endpoint.

The other thing we need to consider when creating the code highlight view is that there's no existing concrete generic view that we can use. We're not returning an object instance, but instead a property of an object instance.

Instead of using a concrete generic view, we'll use the base class for representing instances, and create our own .get() method. In your snippets/views.py add:

from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
As usual we need to add the new views that we've created in to our URLconf. We'll add a url pattern for our new API root in snippets/urls.py:

path('', views.api_root),
And then add a url pattern for the snippet highlights:

path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
```
- Hyperlinking our API
```
Dealing with relationships between entities is one of the more challenging aspects of Web API design. There are a number of different ways that we might choose to represent a relationship:

Using primary keys.
Using hyperlinking between entities.
Using a unique identifying slug field on the related entity.
Using the default string representation of the related entity.
Nesting the related entity inside the parent representation.
Some other custom representation.
REST framework supports all of these styles, and can apply them across forward or reverse relationships, or apply them across custom managers such as generic foreign keys.

In this case we'd like to use a hyperlinked style between entities. In order to do so, we'll modify our serializers to extend HyperlinkedModelSerializer instead of the existing ModelSerializer.

The HyperlinkedModelSerializer has the following differences from ModelSerializer:

It does not include the id field by default.
It includes a url field, using HyperlinkedIdentityField.
Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
We can easily re-write our existing serializers to use hyperlinking. In your snippets/serializers.py add:

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
Notice that we've also added a new 'highlight' field. This field is of the same type as the url field, except that it points to the 'snippet-highlight' url pattern, instead of the 'snippet-detail' url pattern.

Because we've included format suffixed URLs such as '.json', we also need to indicate on the highlight field that any format suffixed hyperlinks it returns should use the '.html' suffix.


```

- Making sure our URL patterns are named
```
If we're going to have a hyperlinked API, we need to make sure we name our URL patterns. Let's take a look at which URL patterns we need to name.

The root of our API refers to 'user-list' and 'snippet-list'.
Our snippet serializer includes a field that refers to 'snippet-highlight'.
Our user serializer includes a field that refers to 'snippet-detail'.
Our snippet and user serializers include 'url' fields that by default will refer to '{model_name}-detail', which in this case will be 'snippet-detail' and 'user-detail'.
After adding all those names into our URLconf, our final snippets/urls.py file should look like this:

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])
```
- Adding pagination
```
The list views for users and code snippets could end up returning quite a lot of instances, so really we'd like to make sure we paginate the results, and allow the API client to step through each of the individual pages.

We can change the default list style to use pagination, by modifying our tutorial/settings.py file slightly. Add the following setting:

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
Note that settings in REST framework are all namespaced into a single dictionary setting, named REST_FRAMEWORK, which helps keep them well separated from your other project settings.

We could also customize the pagination style if we needed to, but in this case we'll just stick with the default.
```
- Browsing the API
```
If we open a browser and navigate to the browsable API, you'll find that you can now work your way around the API simply by following links.

You'll also be able to see the 'highlight' links on the snippet instances, that will take you to the highlighted code HTML representations.

In part 6 of the tutorial we'll look at how we can use ViewSets and Routers to reduce the amount of code we need to build our API.
```
You should be able to sign in and view the API like this. 

![alt text](./Images/Part-5/Screen%20Shot%202023-07-04%20at%206.30.36%20PM.png)
![alt text](./Images/Part-5/Screen%20Shot%202023-07-04%20at%206.30.45%20PM.png)
![alt text](./Images/Part-5/Screen%20Shot%202023-07-04%20at%206.30.55%20PM.png)
![alt text](./Images/Part-5/Screen%20Shot%202023-07-04%20at%206.31.06%20PM.png)
![alt text](./Images/Part-5/Screen%20Shot%202023-07-04%20at%206.31.14%20PM.png)



#### Part_6 Viewsets and Routers
REST framework includes an abstraction for dealing with ViewSets, that allows the developer to concentrate on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on common conventions.

ViewSet classes are almost the same thing as View classes, except that they provide operations such as retrieve, or update, and not method handlers such as get or put.

A ViewSet class is only bound to a set of method handlers at the last moment, when it is instantiated into a set of views, typically by using a Router class which handles the complexities of defining the URL conf for you.

- Refactoring to use ViewSets


- Binding ViewSets to URLS explicitly


- Trade-offs between views vs viewsets





### References
- https://www.django-rest-framework.org/tutorial/1-serialization/
- https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
- https://www.django-rest-framework.org/tutorial/3-class-based-views/
- https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
- https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
- https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/