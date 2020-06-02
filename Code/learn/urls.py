from django.urls import path
from . import views
app_name = 'learn'
urlpatterns = [
    path('', views.home, name='home'),
    path('tech_list', views.tech_list, name='tech_list'),
    path('Contact', views.Contactt, name='Contact'),
    path('About', views.About, name='About'),
    path('editor', views.editor, name='editor'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('learn/<slug>', views.technology, name='technology'),
]
