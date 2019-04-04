from django.urls import  path
from  . import views




app_name = 'howdy'

urlpatterns = [
 
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.PersonCreate.as_view(), name='person_new'),
    path('person_list', views.PersonList.as_view(),  name='person_list'),
    path('edit/<int:pk>',   views.PersonUpdate.as_view(), name='person_edit'),
    path('delete/<int:pk>', views.PersonDelete.as_view(), name='person_delete'),
    
    path("register/",views.register,name="register"),
    path("logout/",views.logout_request,name="logout"),
    path("login/",views.login_request,name="login"),


  
   

    
]