from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS
# PART 3 OF TUTORIAL CLASS BASED VIEWS

# First Code Snippet:
# Updated
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# Second Code Snippet:
# Original
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# The difference between the two snippets is in how the views are defined and associated with the URL patterns.

# In the first code snippet, the views are defined as class-based views (views.SnippetList.as_view() and views.SnippetDetail.as_view()). These class-based views are derived from the APIView class provided by the Django REST Framework (DRF). The .as_view() method is used to convert the class-based views into callable views.

# In the second code snippet, the views are defined as function-based views (views.snippet_list and views.snippet_detail). These are regular Python functions that handle the requests and generate the responses.

# The purpose of the format_suffix_patterns function from rest_framework.urlpatterns is to add support for URL suffixes that specify the desired response format (e.g., .json, .xml). This allows the API to respond with the requested format based on the URL suffix.

# In both code snippets, the format_suffix_patterns function is used to apply the URL suffix patterns to the urlpatterns list, enabling the format suffix behavior for the specified endpoints.

# Overall, the key difference is the choice between class-based views and function-based views to handle the requests, with the associated difference in how the views are referenced in the URL patterns.