from django.urls import path
from .views import ( 
    property_view,  
    show_properties,  
    agent_request,
    search_properties,
)

from . import views
app_name = "buildings"

urlpatterns=[
    path('<int:pk>/', property_view, name='property_view'), # Used for each individual page 
    path('search/', search_properties, name='search_properties'),       # search and redirect 
    path('ver_propiedades/<str:status>/', show_properties, name='all_properties'),# redirect from home to
    path('contact_agent/', agent_request, name='contact_agent'),   # Return the last
]
#Find a a way to pass  parameter such that it reuturns the latest n properties . 