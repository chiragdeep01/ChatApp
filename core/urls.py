from django.urls import path
from . import views
from django.contrib.auth import views as authviews
urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('signup/',views.signupPage,name = 'signup'),
    path('logout/',authviews.LogoutView.as_view(),name = 'logout'),
    path('login/',authviews.LoginView.as_view(template_name = 'core/login.html'),name = 'login')
]