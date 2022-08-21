from django.contrib import admin
from .models import Variation,VariationOne,StaticPhoto,SmartArchive,SmartStructure,SmartTemplate,FileListingUploader,DynamicPhoto
# Register your models here.
admin.site.register(FileListingUploader)
admin.site.register(Variation)
admin.site.register(VariationOne)
admin.site.register(SmartArchive)
admin.site.register(SmartStructure)
admin.site.register(SmartTemplate)
admin.site.register(StaticPhoto)
admin.site.register(DynamicPhoto)