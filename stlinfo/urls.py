from django.urls import path

from .views import (
    stlinfo_detail_view, 
    stlinfo_create_view,
)
app_name = "stlinfo"
urlpatterns = [
    path('', stlinfo_create_view, name ='home'),
    path('stl/<int:stl_id>', stlinfo_detail_view),
]
