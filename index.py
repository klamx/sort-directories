#!/usr/bin/python3

import os.path
import shutil
from pathlib import Path
from tkinter import ttk
from tkinter import filedialog
from tkinter import *

class App:
    def __init__(self, window, file_path, sort_path):
        self.window = window
        self.window.title('Sort Directories')
        self.sort_path = sort_path
        self.file_path = file_path

        self.dirs = ['media', 'img', 'text', 'packages', 'code', 'other']
        self.exts = [
            ['.mov', '.mp4', '.ogg', '.mp3'],
            ['.png', '.jpg', '.jpeg', '.gif'],
            ['.txt', '.docx', '.doc', '.pdf'],
            ['.deb', '.AppImage'],
            ['.py', '.c', '.cpp', '.js', '.css', '.html', '.json', 'cs']
        ]

        # Browser
        self.browse_label = Label(master = window, text = 'Browse your directory:')
        self.browse_label.grid(row = 0, column = 0)
        self.folder_path = StringVar(value = self.sort_path)
        self.folder_label = Label(master = window, borderwidth = 2, relief = 'sunken', textvariable = self.folder_path)
        self.folder_label.config(bg = 'white')
        self.folder_label.grid(row = 1, column = 0)
        self.browse_button = Button(text = 'Explore', command = self.browse_button)
        self.browse_button.grid(row = 1, column = 1)

        # Make directories
        self.mkdir_label = Label(master = window, text = 'Make directories:')
        self.mkdir_label.grid(row = 2, column = 0)
        self.mkdir_button = Button(text = 'Make directories', command = self.make_dirs)
        self.mkdir_button.grid(row = 3, columnspan = 2, sticky = W + E)

        # Sort files
        self.sort_button = Button(text = 'Sort files', command = self.sort)
        self.sort_button.grid(row = 4, columnspan = 2, sticky = W + E)
        

    def browse_button(self):
        dirname = filedialog.askdirectory()
        if str(self.folder_path.get()) != '':
            self.folder_path.set(dirname)
            file = open(self.file_path, 'w')
            x = os.path.abspath(str(self.folder_path.get()))
            # x += '/'
            file.write(x)
            file.close()

            self.sort_path = os.path.abspath(str(self.folder_path.get()))
            self.sort_path += '/'

    def make_dirs(self):
        for dir in self.dirs:
            if not os.path.exists(self.sort_path + dir):
                os.mkdir(self.sort_path + dir)


    def sort_files(self, file, ext):
        file_path = Path(self.sort_path + file)
        if file_path.is_file() or file_path.is_dir():
            for ls in self.exts:
                for ex in ls:
                    if ex == ext:
                        shutil.copy(self.sort_path + file, self.sort_path + self.dirs[self.exts.index(ls)])
                        os.remove(self.sort_path + file)

        # other extension
        if file_path.is_file():
            if ext != '':
                shutil.copy(self.sort_path + file, self.sort_path + self.dirs[5])
                os.remove(self.sort_path + file)
            
            if ext == '' and file != self.dirs[0] and file != self.dirs[1] and file != self.dirs[2] and file != self.dirs[3] and file != self.dirs[4]:
                shutil.copy(self.sort_path + file, self.sort_path + self.dirs[5])
                os.remove(self.sort_path + file)


    def sort(self):
        for file in os.listdir(self.sort_path):
            fileName, ext = os.path.splitext(file)
            self.sort_files(file, ext)
        


if __name__ == '__main__':
    file_path = 'path.txt'
    sort_path = ''
    if os.path.isfile(file_path):
        file = open(file_path, 'r')
        sort_path = file.read()
        sort_path += '/'
    else:
        file = open(file_path, 'w')

    file.close()
    
    window = Tk()
    application = App(window, file_path, sort_path)
    window.mainloop()