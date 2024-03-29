import time
import urllib.request
import os
import ssl
import dbOperation as dbop

def download_from_url(url, path):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(url, filename=path)
    urllib.request.urlcleanup()

def save_file_on_cos(url, cos, name):
    basic_path = './temp/'
    filename = name + "." + url.split(".")[-1]
    path = basic_path + filename
    os.makedirs(basic_path, exist_ok=True)
    download_from_url(url, path)
    cos.uploadFile(path, filename)
    os.remove(path)
    return filename

# def download_photo(url, name):
#     ssl._create_default_https_context = ssl._create_unverified_context
#     basic_path = './image/'
#     path = basic_path + name + "." + url.split(".")[-1]
#     os.makedirs(basic_path, exist_ok=True)
#     urllib.request.urlretrieve(url,filename = path)
#     urllib.request.urlcleanup()
#     return path



# def download_video(url, name):
#     ssl._create_default_https_context = ssl._create_unverified_context
#     basic_path = './video/'
#     path = basic_path + name + "." + url.split(".")[-1]
#     os.makedirs(basic_path, exist_ok=True)
#     urllib.request.urlretrieve(url,filename = path)
#     urllib.request.urlcleanup()
#     return path

def generate_upload_key(type, user_name):
    return "type={}&user={}".format(type, user_name)

def write_tv_review(db, tv_name, user_name, comment):
    now = time.localtime(time.time())
    now_str = time.strftime('%Y-%m-%d %H:%M:%S', now)
    dbop.write_TV_review(db, tv_name, user_name, comment, now_str)

def show_tv_review(db, tv_name):
    return dbop.show_TV_review(db, tv_name)


def write_hiking_routine(db, place, user_name, description):
    now = time.localtime(time.time())
    now_str = time.strftime('%Y-%m-%d %H:%M:%S', now)
    dbop.write_hiking_routine(db, place, user_name, description, now_str)

def show_hiking_routine(db, place):
    return dbop.show_hiking_routine(db, place)

def write_hiking_photo(db, place, path, username):
    dbop.write_hiking_photo(db, place, path, username)

def show_hiking_photo(db, cos, place):
    result = dbop.show_hiking_photo(db, place)
    path = []
    for res in result:
        res = cos.downloadFile(res["photo_path"])
        path.append(res)
    return path

def write_cookary(db, name, path, username):
    dbop.write_cookary(db, name, path, username)

def show_cookary(db, cos, name):
    result = dbop.show_cookary(db, name)
    path = []
    for res in result:
        res = cos.downloadFile(res["video_path"])
        path.append(res)
    return path