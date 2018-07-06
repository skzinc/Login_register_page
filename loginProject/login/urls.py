from django.urls import path
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    path('', views.user, name="user"),
    path('signup/', views.signup, name="signup"),
    path('hello/', views.hello, name="hello"),
    path('signup/profile/', views.profile, name="profile"),
    path('login/', login, {'template_name':'login.html'})
]
