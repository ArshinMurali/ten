from heroapp import views
from django.urls import path

urlpatterns = [

    path('hero', views.hero, name='hero'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
