from django.shortcuts import render,redirect
from .forms import CreateVariation,CreateVariationOne,UploadFileForm,UploadStaticPhoto,UploadSmartArchive,\
    CreateSmartTemplate,UploadFileListingsForm,UploadPhotosForm
from django.contrib.auth import authenticate, login
from main.models import Account
from .models import Variation,VariationOne,StaticPhoto,SmartArchive,SmartStructure,SmartTemplate,FileListingUploader,DynamicPhoto
from main.views import log_in, check_auth
from uploader.folders_reader import make_folder,get_json_structure
from listings.models import Listing
from django.forms import modelformset_factory
import csv

# Create your views here.
def get_user(request):

    user=Account.objects.get(user=request.user)

    return user


def create_variation(request):

    check_auth(request)


    if request.method == "POST":
        form = CreateVariation(request.POST)
        if form.is_valid():


            name=form.cleaned_data['name_app']
            user = get_user(request)


            if not Variation.objects.filter(account=user,name_app=name).exists():

                var=form.save(commit=False)
                var.account=user
                var_in_ls = var.name_app
                var = var.save()
                vars = Variation.objects.filter(account=user, name_app=var_in_ls)
                var=list(vars)[-1]

                return  redirect(f'/uploader/upload_variation/{var.id}')


            else:
                mes=f'This name "{name}" is exist. You need unique name for variation in our application'
                render(request, 'uploader/create_variation.html', locals())

        else:

            mes = "Form is invalid"
            return render(request, 'uploader/create_variation.html', locals())
    else:
        form = CreateVariation()


    return render(request,'uploader/create_variation.html',locals())



def upload_variation(request,var_id):

    check_auth(request)

    var = Variation.objects.get(id=var_id)
    name = var.name_app

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            handle_uploaded_file(request.FILES['file'],var.id)
            add_vars_from_file(f'uploader/work_file_{var_id}.csv',var)

            return redirect(f'/uploader/upload_variation/{var.id}/uploaded')
    else:
        form = UploadFileForm()



    return render(request,'uploader/upload_variation.html',locals())



# ОПРЕДЕЛЯТЬ СЕПАРАЦИЮ
def add_vars_from_file(path,var):
    with open(path, 'r') as file:
        content = file.readlines()

        vos_old=VariationOne.objects.filter(variation=var)
        vos_old.delete()

        rows = content[1:]
        for row in rows[:11]:
            data=row.split(',')
            option=data[0][1:-1]
            SKU=data[1][1:-1]
            quantity=data[2][1:-1]
            price=data[3].replace("\n",'')[1:-1]

            print(option,SKU,quantity,price)

            vo=VariationOne(variation=var,option=option,SKU=SKU,quantity=quantity,price=price)
            vo.save()



    return


#УДАЛЯТЬ РАБОЧИЙ ФАЙЛ
def handle_uploaded_file(f,id):
    with open(f'uploader/work_file_{id}.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def uploaded_variation(request,var_id):
    check_auth(request)


    var = Variation.objects.get(id=var_id)

    var_ones=list(VariationOne.objects.filter(variation=var))

    if request.method == 'POST': #Кнопка "Upload again"
        return redirect(f'/uploader/upload_variation/{var.id}')


    return render(request,'uploader/uploaded_variation.html',locals())



def my_variations(request):

    check_auth(request)

    user = get_user(request)
    vars=Variation.objects.filter(account=user)


    return render(request, 'uploader/my_variations.html', locals())




def upload_static_photo(request):

    check_auth(request)

    form = UploadStaticPhoto(request.POST, request.FILES or None)


    if request.method == "POST" :

        if form.is_valid():

            user = get_user(request)
            name = form.cleaned_data['name']

            print(form.data)

            if not StaticPhoto.objects.filter(account=user, name=name).exists():
                form=form.save(commit=False)

                form.account=user
                form.save()

                return redirect('/uploader/my_static_photos')

            else:
                mes='Something went wrong'
                print(mes)
        else:
            mes='form is invalid'
            print(mes)
            print(request.user)



    return render(request, 'uploader/upload_static_photo.html', locals())

def my_static_photos(request):

    user = get_user(request)
    photos=StaticPhoto.objects.filter(account=user)

    return render(request, 'uploader/my_static_photos.html', locals())


def smart_archive_uploader(request):

    check_auth(request)

    form=UploadSmartArchive(request.POST, request.FILES)

    if request.method == 'POST' and form.is_valid():

        user = get_user(request)
        name = form.cleaned_data['name']
        if not SmartArchive.objects.filter(account=user, name=name).exists():

            archive = form.save(commit=False)
            archive.account=user
            archive.save()
            mes='Uploaded'

            name=(str(user))

            render(request, 'uploader/smart_archive_uploader.html', locals())

            structure_creating(archive,name)

            mes='Structure created'

            return render(request, 'uploader/smart_archive_uploader.html', locals())

    return render(request, 'uploader/smart_archive_uploader.html', locals())




def structure_creating(archive,user):

    path=make_folder(archive.name,archive.file.path,user)
    structure=get_json_structure(path)

    s=SmartStructure(archive=archive,structure=structure)
    s.save()

    print(archive.file.path)

    return


def my_smart_archives(request):

    check_auth(request)
    user=get_user(request)

    archives=SmartArchive.objects.filter(account=user)


    return render(request, 'uploader/my_smart_archives.html', locals())


def create_smart_template(request,archive_id):

    check_auth(request)

    user = get_user(request)

    archive=SmartArchive.objects.get(id=archive_id)
    structure=SmartStructure.objects.get(archive=archive)

    if request.method == 'POST':
        form = CreateSmartTemplate(request.POST)

        if form.is_valid():

            form = form.save(commit=False)
            form.structure = structure
            form.save()
            mes = 'Saved'
            # print(form.cleaned_data)


            return  render(request, 'uploader/create_smart_template.html', locals())
        else:
            errors=form.errors
            form = CreateSmartTemplate(account=user, structure_=structure.structure['names'])
            return render(request, 'uploader/create_smart_template.html', locals())
    else:

        form = CreateSmartTemplate(account=user, structure_=structure.structure['names'])

    mes='тут должна быть форма смарт темплейта но пока держи структуру данных'


    return render(request, 'uploader/create_smart_template.html', locals())


def edit_smart_template(request,template_id):

    check_auth(request)
    user = get_user(request)

    template=SmartTemplate.objects.get(id=template_id)
    structure = template.structure


    if request.method == 'POST':
        form = CreateSmartTemplate(request.POST,instance=template)

        if form.is_valid():

            form = form.save(commit=False)
            form.save()
            mes = 'Saved'

            return render(request, 'uploader/create_smart_template.html', locals())
        else:
            errors = form.errors
            form = CreateSmartTemplate(instance=template, account=user, structure_=structure.structure['names'])
            return render(request, 'uploader/create_smart_template.html', locals())
    else:

        form = CreateSmartTemplate(instance=template,account=user, structure_=structure.structure['names'])

    mes = 'Edit Smart template'

    return render(request, 'uploader/create_smart_template.html', locals())



def upload_listings_file(request):

    check_auth(request)
    user = get_user(request)

    if request.method == 'POST' and 'save_listings' not in dict(request.POST):
        form = UploadFileListingsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.account=user
            form.save()
            print("ятут")

            file_path=form.file.path
            # check_file () проверить файл на ограничения
            listings=create_listings_form_file(file_path,request)

            token=dict(request.POST)['csrfmiddlewaretoken'][0]
            print(token)
            globals()[f'listings_{token}']=listings

        # if 'save_listings' not in dict(request.POST):
        #     render(request, 'uploader/upload_file_listing.html', locals())
        #
        # elif 'save_listings' in dict(request.POST):
        #     for listing in listings:
        #         listing.save()

            return redirect('uploaded_listing_preview',token=token)


    else:
        form = UploadFileListingsForm()

    return render(request, 'uploader/upload_file_listing.html', locals())




def uploaded_listing_preview(request,token):
    print('request',request.method)
    listings = globals()[f'listings_{token}']

    if 'save_listings' in dict(request.POST):
        print(listings)
        for listing in listings:
            listing.save()
        return redirect('listings')
    else:
        return render(request, 'uploader/upload_file_listing.html', {'listings':listings})




def create_listings_form_file(path,request):

    check_auth(request)
    user = get_user(request)

    listings=[]
    lines=[]

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for line in reader:
            lines.append(line)

        for data in lines[2:]:



            for i in [0,7,13,14,15]:
                data[i]=check_int_data(data[i])

            for i in [11,16]:
                data[i]=check_TF_data(data[i])

            try:
                listing=Listing(listing_id=data[0],sku=data[1],title=data[2],description=data[3],tags=data[4],price=data[5],
                                currency_code=data[6],quantity=data[7],
                                who_made=data[10],is_customizable=data[11],when_made=data[12],category_id=data[13],
                                taxonomy_id=data[14],shipping_template_id=data[15],is_supply=data[16],photo_main=data[17],
                                photo2=data[18],photo3=data[19],photo4=data[20],photo5=data[21],photo6=data[22],photo7=data[23],
                                photo8=data[24],photo9=data[25],photo10=data[26],materials=data[27],occasion=data[28])



                listing.account=user
                try:
                    listing.primary_variation=Variation.objects.get(account=user,name_app=data[8])
                except :
                    listing.primary_variation=None
                try:
                    listing.secondary_variation = Variation.objects.get(account=user, name_app=data[9])
                except :
                    listing.secondary_variation=None
                listing.is_etsy=False


                listings.append(listing)
            except Exception as e:
                print('bad line',line,e)

    return listings

def check_int_data(data):
    try:
        data=int(data)
    except:
        data=None
    return data

def check_TF_data(data):
    data_=None
    if data=='1':
        data_=True
    elif data=='0':
        data_=False
    return data_


def upload_dynamic_photos(request):

    check_auth(request)
    user = get_user(request)

    if request.method == 'POST':
        formset = UploadPhotosForm(request.POST, request.FILES,)
        if formset.is_valid():
            print(request.FILES)
            for photo in dict(request.FILES)['photo']:
                # this helps to not crash if the user
                # do not upload all the photos

                print(photo)
                photo = DynamicPhoto(photo=photo,account=user)
                photo.save()

            return redirect('my_dynamic_photos')
    else:
        formset = UploadPhotosForm( )

    return  render(request,'uploader/upload_dynamic_photos.html',locals())



def my_dynamic_photos(request):

    user = get_user(request)
    photos=DynamicPhoto.objects.filter(account=user)

    return render(request, 'uploader/my_dynamic_photos.html', locals())
