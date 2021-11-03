from django.urls import path

from users import views

urlpatterns = [
    path('', views.UsersView.as_view()),
    path('login', views.LoginView.as_view()),
    path('register', views.RegisterView.as_view())
]
