from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # URL pattern for retrieving a list of snippets
    # 'snippets/': This pattern corresponds to the views.snippet_list function or view, which is responsible for retrieving a list of snippets. 
    # It doesn't require a specific pk (primary key) value as a parameter.


    path('snippets/', views.snippet_list),  
    # URL pattern for retrieving, updating, or deleting a specific snippet
    # 'snippets/<int:pk>/': This pattern corresponds to the views.
    # snippet_detail function or view, which is responsible for retrieving, updating, or deleting a specific snippet. 
    # The <int:pk> part is a path converter that matches an integer value and assigns it to the pk parameter of the view function. 
    # The pk represents the primary key or identifier of a specific snippet.
    path('snippets/<int:pk>/', views.snippet_detail),  
]


# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# PART 2 OF TUTORIAL REQUESTS AND RESPONSES
# Now update the snippets/urls.py file slightly, to append a set of format_suffix_patterns in addition to the existing URLs.
# We don't necessarily need to add these extra url patterns in, but it gives us a simple, clean way of referring to a specific format.

# BROWSABLITY
# Because the API chooses the content type of the response based on the client request, it will, by default, return an HTML-formatted representation of the resource when that resource is requested by a web browser. This allows for the API to return a fully web-browsable HTML representation.

# Having a web-browsable API is a huge usability win, and makes developing and using your API much easier. It also dramatically lowers the barrier-to-entry for other developers wanting to inspect and work with your API.

# See the browsable api topic for more information about the browsable API feature and how to customize it.

# https://www.django-rest-framework.org/topics/browsable-api/

# Normally this url suffix approach will make it so our http://127.0.0.1:8000/snippets route would default to a template with the .html suffix, but we don't have any templates in this project, so it will just return a 404 error.
# We would need to do http://127.0.0.1:8000/snippets.json to get back a formatted version of the data.
# instead I simply added back the jsonResponse to the views.py file, and it works fine. and displays the data as expected on http://127.0.0.1:8000/snippets
# FORMAT SUFFIXES ARE OPTIONAL, DON'T FEEL COMPELLED TO USE THIS FEATURE IF YOUR API DOESN'T NEED IT.

urlpatterns = format_suffix_patterns(urlpatterns)

# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS

# Part 3 is continued in the snippets folder in the urls.py file, I renamed this one to urls-Parts-1-2.py to avoid confusion and to make it easier to find the code for part 3, check that out, this code won't be used now.