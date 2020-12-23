import os.path
import shutil
from pathlib import Path

downloadPath = os.path.abspath('/home/alejandro/Descargas/')
downloadPath += '/'
mediaExt = ['.mov', '.mp4', '.ogg', '.mp3']
imgExt = ['.png', '.jpg', '.jpeg', '.gif']
textExt = ['.txt', '.docx', '.doc', '.pdf']
packExt = ['.deb', '.AppImage']

def sort(file, ext):
    filePath = Path(downloadPath + file)
    if filePath.is_file() or filePath.is_dir():
        for i in mediaExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + 'multi-media')
                os.remove(downloadPath + file)

        for i in imgExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + 'imagenes')
                os.remove(downloadPath + file)

        for i in textExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + 'texto')
                os.remove(downloadPath + file)

        for i in packExt:
            if ext == i:
                shutil.copy(downloadPath + file, downloadPath + 'paquetes')
                os.remove(downloadPath + file)

    if filePath.is_file():
        if ext != '':
            shutil.copy(downloadPath + file, downloadPath + 'otros')
            os.remove(downloadPath + file)
        
        if ext == '' and file != 'videos' and file != 'imagenes' and file != 'texto' and file != 'paquetes':
            shutil.copy(downloadPath + file, downloadPath + 'otros')
            os.remove(downloadPath + file)

if __name__ == "__main__":
    for file in os.listdir(downloadPath):
        fileName, ext = os.path.splitext(file)
        sort(file, ext)
