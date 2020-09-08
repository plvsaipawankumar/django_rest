from django.contrib import admin
from django.urls import path,include
from .models import Fapp
from .views import Fapp_List,Fapp_Particular

urlpatterns = [
    path('fappget',Fapp_List.as_view()),
    path('fapppost/<str:name>',Fapp_Particular.as_view()),
    

    # path('pfapp/<char:naam>/',PFapp),
]
