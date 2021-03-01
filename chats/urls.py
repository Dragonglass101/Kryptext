from django.contrib import admin
from django.urls import path
from chats import views

admin.site.site_header = "Kryptext login"
admin.site.site_title = "Login"
admin.site.index_title = "Welcome to Kryptext :)"

urlpatterns = [
    path("", views.index_1, name='chats'),
    path("description/", views.description, name='description'),
    path("aboutus/", views.aboutus, name='about'),
    path("signin/", views.signin, name='signin'),
    path("login/", views.loginpage, name='login')
]
