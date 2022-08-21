from django.urls import path
from . import views


urlpatterns = [
    path('listing_<listing_id>', views.listing_page),
    path('catalog', views.listing_catalog,name='listings'),
    path('pre_uploaded', views.listing_preuploaded),
]

