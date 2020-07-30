from django.urls import path
from cm import views
open_name='cm'

urlpatterns= [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('child',views.child,name="child"),
    path('sam',views.sam,name="sam"),

]