from django.urls import path
from cm import views
open_name='cm'

urlpatterns= [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('tem/',views.tem,name="tem"),
    path('sam',views.sam,name="sam"),

]