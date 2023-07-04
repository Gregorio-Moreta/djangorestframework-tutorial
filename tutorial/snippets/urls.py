# PART 4 OF TUTORIAL Authentication & Permissions
# PART 4 OF TUTORIAL Authentication & Permissions
# PART 4 OF TUTORIAL Authentication & Permissions

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # Finally we need to add those user views into the API, by referencing them from the URL conf. Add the following to the patterns in snippets/urls.py.
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)