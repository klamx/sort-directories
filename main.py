import os
import sys
import shutil
import time


downloadPath = os.path.abspath('/home/alejandro/Descargas/')
downloadPath += '/'
videoExt = ['.mov', '.mp4']
imgExt = ['.png', '.jpg', '.jpeg', '.gif']
textExt = ['.txt', '.docx', '.doc', '.pdf']
packExt = ['.deb', '.AppImage']

def sort(file, ext):
    for i in videoExt:
        if ext == i:
            shutil.move(downloadPath + file, downloadPath + 'videos')

    for i in imgExt:
        if ext == i:
            shutil.move(downloadPath + file, downloadPath + 'imagenes')

    for i in textExt:
        if ext == i:
            shutil.move(downloadPath + file, downloadPath + 'texto')

    for i in packExt:
        if ext == i:
            shutil.move(downloadPath + file, downloadPath + 'paquetes')

    if ext != '':
        shutil.move(downloadPath + file, downloadPath + 'otros')
    
    if ext == '' and file != 'videos' and file != 'imagenes' and file != 'texto' and file != 'paquetes':
        shutil.move(downloadPath + file, downloadPath + 'otros')

if __name__ == "__main__":
    for file in os.listdir(downloadPath):
        fileName, ext = os.path.splitext(file)
        sort(file, ext)
