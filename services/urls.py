from django.urls import path
from . import views

urlpatterns = [
    path('lender', views.servicesLender, name='ucc-services-lender'),
    path('owner', views.servicesOwner, name='ucc-services-owner'),
    path('building', views.servicesBuilding, name='ucc-services-building'),
    path('litigation', views.servicesLitigation, name='ucc-services-litigation'),

]