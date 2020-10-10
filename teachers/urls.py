from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addteacher/', views.add_teacher, name='addteacher'),
    path('addpost/', views.add_post, name='addpost'),
    path('addthing/', views.add_thing, name='addthing'),
    path('showdata/', views.show_data, name='showdata'),
]