"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    # Include URLs from the 'snippets.urls' module
    # A single URL pattern defined by path(''). 
    # The include() function is used to include URLs from the snippets.urls module.
    # The include() function is a Django utility that allows you to include another URLconf module, such as snippets.urls, to the current URL configuration. 
    # It effectively delegates the handling of URLs to another URLconf module, allowing for modularity and separation of concerns.
    # So, in the pseudocode, the 'snippets.urls' module is included at the root URL pattern ''. 
    # This means that any URLs defined in the snippets.urls module will be included and accessible under the root URL.

    path('', include('snippets.urls')),  
]
