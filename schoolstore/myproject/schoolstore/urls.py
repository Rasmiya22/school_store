from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('new/',views.new,name='new'),
    path('register/',views.register,name='register'),

    path('course/computer-science/', views.computer_science, name='computer_science'),
    path('course/mechanical/', views.mechanical, name='mechanical'),
    path('course/electrical/', views.electrical, name='electrical'),
    path('course/electronics/', views.electronics, name='electronics'),
    path('course/production/', views.production, name='production')

]