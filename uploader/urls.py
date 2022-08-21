from django.urls import path
from . import views


urlpatterns = [
    path('create_variation', views.create_variation),
    path('upload_variation/<var_id>', views.upload_variation),
    path('upload_variation/<var_id>/uploaded', views.uploaded_variation),
    path('my_variations', views.my_variations, name='my_variations'),
    path('upload_static_photo', views.upload_static_photo),
    path('my_static_photos', views.my_static_photos),
    path('smart_archive_uploader', views.smart_archive_uploader),
    path('my_smart_archives', views.my_smart_archives),
    path('create_smart_template/<archive_id>', views.create_smart_template),
    path('edit_smart_template/<template_id>', views.edit_smart_template),
    path('upload_file_listing',views.upload_listings_file),
    path('upload_file_listing/preview_<token>',views.uploaded_listing_preview,name='uploaded_listing_preview'),
    path('upload_dynamic_photos',views.upload_dynamic_photos),
    path('my_dynamic_photos',views.my_dynamic_photos,name='my_dynamic_photos'),


]

