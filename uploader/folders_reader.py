import os
import zipfile
import json



def make_folder(archive_name,path_to_archive,user):

    path_to_folder=f'{path_to_archive.replace(".zip","")}'

    with zipfile.ZipFile(path_to_archive, 'r') as zip_ref:
        zip_ref.extractall(path_to_folder)

    return path_to_folder


def get_json_structure(path):

    paths=get_all_final_paths(path)

    names={'folder0':set_names(paths,-2),
           'folder1':set_names(paths,-3),
           'folder2':set_names(paths,-4),
           'photo_names':set_names(paths,-1)}

    structure={'names':names,'paths':paths}

    return structure


def get_all_final_paths(path):

    #СДЕЛАТЬ ТОЛЬКО ОТОНОСИТЕЛЬНЫЕ ПАТЧИ

    paths = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        paths += [os.path.join(dirpath, file) for file in filenames]

    paths_f=[]

    for p in paths:


    #КАК ТО СРЕЗАТЬ ФОРМАТЫ
        p=p.replace(".jpg",'')
        p = p.replace(".JPG", '')
#КАК ТО НЕ ЧИТАТЬ ЭТИ СИСТЕМНЫЕ ПАПКИ
        if """__MACOSX""" not in p:
            paths_f.append(p)

    return paths_f


def path_slicer(path,N):

    name=path.split('/')[N]

    return name


def set_names(paths,N):

    set_=set([path_slicer(path, N) for path in paths])
    set_=[{'name':n} for n in set_]


    return set_


#