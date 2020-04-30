from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='ucc-homepage'),
    path('thankyou/', views.thankyou, name='contact-thank-you'),
]