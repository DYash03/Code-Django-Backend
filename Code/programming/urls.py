from django.urls import path
from . import views
app_name = 'programming'
urlpatterns = [
    path('', views.pro_list, name='pro_list'),
    path('postComment', views.postComment, name='postComment'),
    path('del/<int:sno>', views.deleteComment, name='deleteComment'),
    path('category/<str:category>', views.pro_category, name='pro_category'),
    path('<slug>', views.program, name='program'),
]
