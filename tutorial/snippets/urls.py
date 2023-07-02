from django.urls import path
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
