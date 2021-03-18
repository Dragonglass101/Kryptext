from django.contrib import admin
from django.urls import path
from chats import views

admin.site.site_header = "Kryptext login"
admin.site.site_title = "Login"
admin.site.index_title = "Welcome to Kryptext :)"

urlpatterns = [
    path("", views.index_1, name='home_1'),
    path("description/", views.description, name='description'),
    path("aboutus/", views.aboutus, name='about'),
    path("signin/", views.signin, name='signin'),
    path("login/", views.loginpage, name='login'),
    path("after@login**!home%$page;alsdvjioanerg239872938kjrhgowergw/", views.index_2, name='home_2'),
    path("after@login**!home%$page;alsdvjioanerg239872938kjrhgowergw/compose", views.compose, name='compose'),
    path("after@login**!home%$page;alsdvjioanerg239872938kjrhgowergw/chat_history", views.chat_history, name='chat_history')
]
