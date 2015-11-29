# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile as sc
from merge_sounds import *
from create_track import *

"""
Moduł z funkcją do tworzenia piosenki ze ścieżek.
"""

print('Modul o nazwie: ' + __name__ + ' zostal wczytany.')

def create_song(dir):
    
    """
    Funkcja tworząca piosenkę.
    Argument:
        * dir - folder z plikami piosenki
    """
    
    # wczytujemy plik z własnościami piosenki
    defs = open(dir + '/defs.txt', 'r')
    properties = eval(defs.read())
    defs.close()

    # wczytujemy plik z częstotliwościami nutek
    freq = open('./notes.txt', 'r')
    notes = eval(freq.read())
    freq.close()
    
    # wczytujemy interesujące nas własności
    bpm = properties['bpm']
    
    # wczytujemy plik z kolejnością odgrywanych ścieżek
    song_table = np.genfromtxt(dir + '/song.txt', dtype = 'str')

    # tworzymy słownik ścieżek oraz ich przesunięć i je wczytujemy (by szybciej działało)
    tracks = np.unique(song_table)
    tracks_dict = dict()
    tracks_delays = dict()
    for x in tracks:
        track, track_delay = create_track(dir, x, bpm, notes)
        tracks_dict[x] = track
        tracks_delays[x] = track_delay
    
    # tworzymy piosenkę
    fs = 44100 # częstotliwość
    delay = 0 # przesunięcie ze względu na wczytywane linie ze ścieżkami
    song = np.zeros((0,2))
    for line in song_table:
        song = merge_sounds(song, tracks_dict[line], delay)
        delay += tracks_delays[line]
    sc.write(dir + '.wav', fs, np.int16(song / np.amax(np.abs(song)) * 32767))  
