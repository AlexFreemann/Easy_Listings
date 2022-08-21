
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index,name='home'),
    path('contact', views.contact_us),
    path('about', views.about),
    path('login', views.log_in),
    path('registration', views.registration),
    path('account', views.account),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change_password', views.change_passport, name='change_password'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('set_new_password', views.set_new_password, name='set_new_password'),



]
