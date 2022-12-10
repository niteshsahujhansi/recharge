from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/registration/', views.registration, name='registration'),
    path('accounts/login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('combo/', views.combo, name='combo'),
    path('internet/', views.internet, name='internet'),
    path('talk/', views.talk, name='talk'),
    path('browse/', views.browse, name='browse'),
    path('checkout/', views.checkout, name='checkout'),
]