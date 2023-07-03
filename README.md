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
#### Part_1
Follow along here
- https://www.django-rest-framework.org/tutorial/1-serialization/

I even left the code that we eventually replaced. 
I added comments to it so as to add context about why it was replaced, from pure django to djangorestframework.

#### Part_2
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

#### Part_3
- https://www.django-rest-framework.org/tutorial/3-class-based-views/


### Summary
#### Part_1

At the end of part 1, you should be able to perform full CRUD functionality. 

There is still a lot of djangorestframework specific modifications required to make it a RESTful API, but those features are explained in the later tutorials.

I have created models, serializers, urls, views, a project called tutorial, and an app called snippets. So far we are using the default sqlite3 database.

I added the snippets app to the settings.py for my tutorial project inside of the install_apps list.

I ran makemigrations and migrate so my models should be synched with the database as well.

If I missed something I'll add it later. Please make an issue if you want to bring something to my attention. Thank you, kindly!

#### Part_2
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

#### Part_3
I made a new views file for this part, the code is more concise and uses the APIView class as explained in the new views file comments. Essentially it handles a lot of scenarios for you out of the box so you don't need to manually configure everything in your views like before. It will allow us to build features more quickly.

### References
- https://www.django-rest-framework.org/tutorial/1-serialization/
- https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
- https://www.django-rest-framework.org/tutorial/3-class-based-views/
- https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
- https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
- https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/