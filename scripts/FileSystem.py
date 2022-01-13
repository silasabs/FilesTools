# script created with the purpose of automating everyday tasks in addition to implementing security functions 
# such as the generation of hash in SHA256, which has a certain resistance to collision in addition to verifying
# the integrity of the files.

import tkinter as tk
from tkinter import filedialog as dlg
import hashlib
import time
import os
import shutil

# hide default tk windows
root = tk.Tk()
root.withdraw()


def clear_display():
    """
    function responsible for cleaning the terminal.
    """
    time.sleep(2.8)
    # for linux  
    # return os.system('clear') or None
    return os.system('cls') or None


def fileName(path_file):
    """
    function responsible for returning the file name.
    """
    # Extract file name.
    path_file = os.path.splitext(path_file)[0]
    file_name = path_file.split('/')[-1]
    return file_name


def load_path():
    """
    Function responsible for selecting the requested directory.
    """
    path = dlg.askdirectory()
    return str(path)


def load_file():
    """
    Function responsible for selecting the requested file.
    """
    path = dlg.askopenfilename()
    return str(path)


def load_files():
    """
    Function responsible for returning a series of files.
    """
    path = dlg.askopenfilenames()
    return str(path)


def organizer(path):
    """
    function responsible for organizing the files of a directory assigning folders for each extension found.
    param path: directory to be organized.
    """
    # list files in directory.
    files = os.listdir(path)

    for index in files:
        # separates the file name and its respective extension.
        filename, extension = os.path.splitext(index)
        extension = extension[1:]
        # checks if a folder with the extension to be sorted already exists.
        if os.path.exists(path + '/' + extension):
           # move all files to the already existing folder
           shutil.move(path + '/' + index, path + '/' + extension + '/' + index)
        # creates folders by extension and moves them to their respective folder.
        else: 
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + index, path + '/' + extension)


def hash(filepath):
    """
    function responsible for generating a hash of a given file in SHA256.
    param filepath: directory where the file is located. 
    """
    with open(filepath, 'rb') as stream:
        hash = hashlib.sha256(stream.read())
    return hash.hexdigest()


def compression(path):
    """
    function responsible for compressing the files in a directory.
    param path: directory to be compressed.
    """
    shutil.make_archive(path, 'zip', path)