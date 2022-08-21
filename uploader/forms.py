from django import forms
from .models import VariationOne,Variation,StaticPhoto,SmartArchive,SmartTemplate,SmartStructure,FileListingUploader,DynamicPhoto

#

class CreateVariation(forms.ModelForm):

    name_etsy = forms.CharField(label='Name in listing on Etsy', widget=forms.TextInput(attrs={'class': 'form-control', }))
    name_app = forms.CharField(label='Name for Your account here', widget=forms.TextInput(attrs={'class': 'form-control', }))


    class Meta:
        model = Variation
        fields = ('name_app', 'name_etsy')



class CreateVariationOne(forms.ModelForm):
    # variation = forms.ModelChoiceField(queryset=Variation.objects.filter(user='1'),)
    option = forms.CharField(label='Option', max_length=25)
    SKU = forms.IntegerField(label='SKU')
    quantity = forms.IntegerField(label='Quantity')
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)


    class Meta:
        model = VariationOne
        exclude=['variation']

class UploadFileForm(forms.Form):
    file = forms.FileField()


class UploadStaticPhoto(forms.ModelForm):

    class Meta:
        model = StaticPhoto
        fields=['name','photo']


class UploadSmartArchive(forms.ModelForm):

    class Meta:
        model = SmartArchive
        fields= ['name','file']


class CreateSmartTemplate(forms.ModelForm):

    separation = forms.ChoiceField(choices=([('1', 'Each final folder (folder0) is ONE listing'),
                                             ('2', 'Each final photo is ONE listing'), ('3', 'Some listings in final folder, write number next field'), ]))

    separation_number=forms.IntegerField(max_value=10,min_value=2)

    photo1 = forms.CharField(widget=())
    photo2 = forms.CharField(widget=())
    photo3 = forms.CharField(widget=())
    photo4 = forms.CharField(widget=())
    photo5 = forms.CharField(widget=())


    class Meta:
        model=SmartTemplate
        exclude=['structure']


    def __init__(self, *args, **kwargs):

        account=None
        structure_=None

        if 'account' in kwargs:
            account= kwargs.get('account', None)
            kwargs.pop('account')
            structure_= kwargs.get('structure_', None)
            kwargs.pop('structure_')

        super(CreateSmartTemplate, self).__init__(*args, **kwargs)

        if account:
            print('account',account)
            self.fields['variation'].queryset= Variation.objects.filter(account=account)

            #СДЕЛАТЬ РЕАЛЬЫНЕ ФОТКИ А НЕ ИМЕНА
            for i in range(1,6):
                self.fields[f'photo{i}'].widget=forms.Select(choices=get_img_options(account,structure_))


            # ([('1', '1'), ('2', '2'), ('знчение для формы', 'значение в меню'), ])
def get_img_options(account, structure):

    img_options = ([(None, 'No Photo')]
                + [(img_ob.name, img_ob.name) for img_ob in StaticPhoto.objects.filter(account=account)]
                + [(i['name'], i['name']) for i in structure['photo_names']])

    return img_options

class UploadFileListingsForm(forms.ModelForm):

    class Meta:
        model=FileListingUploader
        fields=['name','file']



class UploadPhotosForm(forms.ModelForm):
    photo = forms.ImageField(label='Image',widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model=DynamicPhoto
        fields = ('photo', )
