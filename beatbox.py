#!/home/smender/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sys
import os.path
import zipfile
from create_song import *

"""
Skrypt tworzący piosenkę, która została podana jako argument.
"""

dir = sys.argv[1]

# robimy poprawkę na nazwę folderu,
# jeśli '/' jest na końcu w komendzie
if dir[-1:] == '/':
    dir = dir[:-1]

print("Piosenka " + dir + ".wav jest tworzona! Prosze czekac!")
    
# sprawdzamy czy plik *.zip
dir_tmp = dir + '.zip'
if os.path.isfile(dir_tmp): 
    with zipfile.ZipFile(dir_tmp, "r") as zip:
        zip.extractall('/tmp/')
        dir = '/tmp/' + dir

# tworzymy piosenkę
create_song(dir)
print("Piosenka " + dir + ".wav zostala stworzona!")
