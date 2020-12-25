#!/usr/bin/python3

import os.path
import shutil
from pathlib import Path

downloadPath = os.path.abspath('/home/alejandro/Descargas/')
downloadPath += '/'

multi = 'multi-media'
img = 'imagenes'
txt = 'texto'
packages = 'paquetes'
code = 'codigo'
others = 'otros'


# Make dirs
if not os.path.exists(downloadPath + multi):
    os.mkdir(downloadPath + multi)

if not os.path.exists(downloadPath + img):
    os.mkdir(downloadPath + img)

if not os.path.exists(downloadPath + txt):
    os.mkdir(downloadPath + txt)

if not os.path.exists(downloadPath + packages):
    os.mkdir(downloadPath + packages)

if not os.path.exists(downloadPath + others):
    os.mkdir(downloadPath + others)

if not os.path.exists(downloadPath + code):
    os.mkdir(downloadPath + code)


# Extensions
mediaExt = ['.mov', '.mp4', '.ogg', '.mp3']
imgExt = ['.png', '.jpg', '.jpeg', '.gif']
textExt = ['.txt', '.docx', '.doc', '.pdf']
packExt = ['.deb', '.AppImage']
codExt = ['.py', '.c', '.cpp', '.js', '.css', '.html', '.json', '.cs']


def sort(file, ext):
    filePath = Path(downloadPath + file)
    if filePath.is_file() or filePath.is_dir():
        for i in mediaExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + multi)
                os.remove(downloadPath + file)

        for i in imgExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + img)
                os.remove(downloadPath + file)

        for i in textExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + txt)
                os.remove(downloadPath + file)

        for i in packExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + packages)
                os.remove(downloadPath + file)

        for i in codExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + code)
                os.remove(downloadPath + file)

    # other extension
    if filePath.is_file():
        if ext != '':
            shutil.copy(downloadPath + file, downloadPath + others)
            os.remove(downloadPath + file)
        
        if ext == '' and file != multi and file != img and file != txt and file != packages and file != code:
            shutil.copy(downloadPath + file, downloadPath + others)
            os.remove(downloadPath + file)


if __name__ == "__main__":
    for file in os.listdir(downloadPath):
        fileName, ext = os.path.splitext(file)
        sort(file, ext)
