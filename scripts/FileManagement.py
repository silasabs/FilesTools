# script created with the purpose of automating everyday tasks in addition to implementing security functions 
# such as the generation of hash in SHA256, which has a certain resistance to collision in addition to verifying
# the integrity of the files.

import tkinter as tk
from tkinter import filedialog as dlg
import hashlib
import pyfiglet
import time
import os
import shutil

# hide default tk windows
root = tk.Tk()
root.withdraw()


def fileName(path):
    """
    Function that returns the name of a file.
    """
    path = os.path.splitext(path)[0]
    name_file = path.split('/')[-1]
    return name_file


def extensionName(path):
    """
    Function responsible for returning the extension of a file.
    """
    extension = os.path.splitext(path)[1][1:]
    return extension


def clear_display():
    """
    function responsible for cleaning the terminal.
    """
    time.sleep(2.5)
    # for linux  
    # return os.system('clear') or None
    return os.system('cls') or None


def load_path():
    """
    Function responsible for selecting the requested directory.
    return: directory returned as string.
    """
    path = dlg.askdirectory()
    return str(path)


def load_file():
    """
    Function responsible for selecting the requested file.
    return: directory where the file is located.
    """
    path = dlg.askopenfilename()
    return str(path)


def checkExtension(path, str):
    """
    This function is responsible for checking the extension of a file.
    param path: File path.
    param str: Extension to be compared.

    return flag: returns a boolean about the extent to be checked.
    """
    flag = True
    while extensionName(path) != str:
        print('Unsupported file. Try again')
        path = load_file()

        if path:
            continue
        else:
            print('No files were selected.')
            flag = False
            break
    
    return flag

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

    return: SHA256 requested file hash  
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
