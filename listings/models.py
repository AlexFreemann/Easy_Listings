from django.db import models
from main.models import Account
from uploader.models import Variation



class Listing(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, )
    is_etsy = models.BooleanField('True=on Etsy, False=pre-uploaded', default=False)
    listing_id=models.IntegerField('Listing_id on Etsy',blank=True, default=None,null=True)
    status=models.CharField('Status', max_length=40,blank=True, default=None,null=True)

    sku=models.CharField('SKU',max_length=32,blank=True, default=None,null=True)

    title=models.CharField('Title', max_length=140,blank=True, default=None,null=True)
    description = models.TextField('Description', max_length=5000,blank=True, default=None,null=True)
    language=models.CharField('Language',default='en',max_length=2,blank=True,null=True )

    tags=models.CharField('Tags',max_length=300,blank=True, default=None,null=True)

    who_made=models.CharField('Who made?',max_length=30,blank=True, default=None,null=True)
    is_customizable=models.BooleanField('Is customizable?',null=True)
    when_made=models.CharField('When made?',max_length=30,blank=True, default=None,null=True)
    is_supply=models.BooleanField('Is supply?',null=True)

    category_id=models.IntegerField('Category id',blank=True, default=None,null=True)
    taxonomy_id=models.IntegerField('Taxonomy id',blank=True, default=None,null=True)
    shipping_template_id=models.IntegerField('Shipping Template id',blank=True, default=None,null=True)

    price=models.DecimalField('Price',max_digits=10, decimal_places=2,blank=True, default=None,null=True)
    currency_code=models.CharField('Currency',max_length=3,blank=True, default=None,null=True)
    quantity=models.IntegerField('Quantity',blank=True, default=None,null=True)

    materials=models.CharField('Materials',max_length=300,blank=True, default=None,null=True)
    occasion=models.CharField('Occasion',max_length=300,blank=True, default=None,null=True)

    photo_main = models.URLField('Main Photo',blank=True, default=None,null=True)
    photo2 = models.URLField('Photo2',blank=True, default=None,null=True)
    photo3 = models.URLField('Photo3',blank=True, default=None,null=True)
    photo4 = models.URLField('Photo4',blank=True, default=None,null=True)
    photo5 = models.URLField('Photo5',blank=True, default=None,null=True)
    photo6 = models.URLField('Photo6',blank=True, default=None,null=True)
    photo7 = models.URLField('Photo7',blank=True, default=None,null=True)
    photo8 = models.URLField('Photo8',blank=True, default=None,null=True)
    photo9 = models.URLField('Photo9',blank=True, default=None,null=True)
    photo10 = models.URLField('Photo10',blank=True, default=None,null=True)

    primary_variation=models.ForeignKey(Variation, on_delete=models.CASCADE,blank=True,default=None,
                                        verbose_name='Primary Variation',related_name='primary_variation',null=True)
    secondary_variation=models.ForeignKey(Variation, on_delete=models.CASCADE,blank=True,default=None,
                                          verbose_name='Secondary Variation',related_name='secondary_variation',null=True)


    def __str__(self):
        return f'{self.listing_id}---{self.title}---{self.account}'





class Competitor(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,)
    shop_name=models.CharField('Shop', max_length=20,blank=True,default=None)
    is_sold_lisitngs=models.BooleanField('Is open sold listing?',blank=True)



    def __str__(self):
        return f'{self.shop_name}---{self.account}'



class CompetitorSalesOnDate(models.Model):
    date= models.DateTimeField(editable=False)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE,)
    sales=models.IntegerField('Number of Sales on date')


    def __str__(self):
        return f'{self.shop_name}---{self.account}'



class ListingSales(models.Model):
    date = models.DateTimeField(editable=False)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE, )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, )
    sales = models.IntegerField('Number of Sales on date')

    def __str__(self):
        return f'{self.shop_name}---{self.account}'


class ListingFavorites(models.Model):
    date = models.DateTimeField(editable=False)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE, )
    favorites = models.IntegerField('Number of Likes on date')

    def __str__(self):
        return f'{self.shop_name}---{self.account}'




