from django.urls import path
from .views import index,signin,signup,signout,delete,forms,update,notes_content

urlpatterns = [
    path('',index,name='index'),
    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('logout/',signout,name='logout'),
    path('form/',forms,name='form'),
    path('update/<str:pk>/',update,name='update'),
    path('delete/<str:pk>/',delete,name= 'delete'),
    path('notes/<str:pk>/',notes_content,name='content'),
]
