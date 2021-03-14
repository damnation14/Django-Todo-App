
from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.home,name='Todo-home'),
    path('addact/', views.add_activity,name='Todo-add'),
    path('deleteact/<int:pk>', views.delete_activity,name='Todo-delete'),
    path('searchact/', views.search_activity,name='Todo-search'),
   
]