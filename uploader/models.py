from django.db import models
from main.models import Account
from django_resized import ResizedImageField

class Variation(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,)
    name_etsy=models.CharField('Name for Etsy', max_length=25)
    name_app=models.CharField('Name for App', max_length=25)


    def __str__(self):
        return f'{self.account}---{self.name_app}'


class VariationOne(models.Model):
    variation=models.ForeignKey(Variation,on_delete = models.CASCADE)
    option = models.CharField('Option', max_length=25)
    SKU=models.IntegerField('SKU')
    quantity = models.IntegerField('Quantity')
    price=models.DecimalField('Price',max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.variation.account}---{self.variation.name_app}---{self.option}'

#
class FileListingUploader(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, )
    name = models.CharField('Name', max_length=25)
    file=models.FileField('File', upload_to='listing_files/listings',)

    def __str__(self):
        return f'{self.account}---{self.name}'

# #
# class ArchiveForUploading(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, )
#     name = models.CharField('Name', max_length=25)
#     title_mask= models.CharField('Option', max_length=200)
#     tag_mask=models.CharField('Option', max_length=200)
#     photos_mask=models.CharField('Option', max_length=200)

class SmartArchive(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, )
    name = models.CharField('Name', max_length=25)
    file=models.FileField(upload_to='archives')

    def __str__(self):
        return f'{self.account}---{self.name}'

class SmartStructure(models.Model):
    archive=models.OneToOneField(SmartArchive, on_delete=models.CASCADE)
    structure= models.JSONField('Json Structure')

    def __str__(self):
        return f'{self.archive.account}---{self.archive.name}'


class SmartTemplate(models.Model):

    name=models.CharField('Name this template', max_length=500,blank=False)
    structure=models.ForeignKey(SmartStructure, on_delete=models.CASCADE, )
    separation=models.CharField('Method of separation',max_length=500)#0-folder0, 1-each file, 2+-separation x files in folder by n
    separation_number = models.IntegerField('Separation number')

    title=models.CharField('Template for title', max_length=140)

    photo1= models.CharField('Photo1', max_length=500, blank=True)
    photo2 = models.CharField('Photo2', max_length=500, blank=True)
    photo3 = models.CharField('Photo3', max_length=500, blank=True)
    photo4 = models.CharField('Photo4', max_length=500, blank=True)
    photo5 = models.CharField('Photo5', max_length=500, blank=True)

    variation=models.ForeignKey(Variation,on_delete=models.CASCADE, blank=True)


class StaticPhoto(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, )
    name = models.CharField('Name for App your photo', max_length=25)
    photo = models.ImageField('Photo', upload_to='images/static/static_photos',blank=True,default=True)

    def __str__(self):
        return f'{self.account}---{self.name}'

class DynamicPhoto(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, )
    archive=models.ForeignKey(SmartArchive,on_delete=models.CASCADE,
                              verbose_name='Name of Archive, Manually uploaded is empty',
                              max_length=25,blank=True,null=True)
    path=models.CharField('Path in smart archive', max_length=500,blank=True)
    name = models.CharField('Name for App your photo', max_length=25,blank=True)
    photo = models.ImageField('Photo', upload_to='images/static/dynamic_photos',blank=True,default=True)

    def __str__(self):
        return f'{self.account}---{self.name}'


