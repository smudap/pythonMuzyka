# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile as sc
from merge_sounds import *
from sounds import *

"""
Moduł z funkcją do tworzenia ścieżki z sampli, nutek i instrumentów.
"""

print('Modul o nazwie: ' + __name__ + ' zostal wczytany.')

def create_track(dir, track_file, bpm, notes):
    
    """
    Funkcja tworząca ścieżkę.
    Argumenty:
        * dir - folder z plikami piosenki
        * track_file - numer pliku ze ścieżką
        * bpm - beats per minute
        * notes - słownik z częstotliwościami nutek
    """
    
    # wczytujemy plik z kolejnością odgrywanych sampli
    track_table = np.genfromtxt(dir + '/track' + track_file + '.txt',
                                dtype = 'str', comments = '"') 
    
    # zczytujemy długości elementów by wiedzieć czy sample czy nutka czy instrument
    n, m = np.shape(track_table)
    lengths = np.zeros((n, m))
    for i in np.arange(n):
        for j in np.arange(m):
            lengths[i, j] = len(track_table[i, j])
    
    # tworzymy słownik pomocniczy z samplami, nutkami i instrumentami (by szybciej działało)
    music_dict = dict()
    
    # dodajemy sample do słownika
    samples = np.unique(track_table[np.where(lengths == 2)])
    for x in samples:
        if x == '--':
            continue
        fs, sample = sc.read(dir + '/sample' + x + '.wav')
        sample = sample / np.amax(sample) # normujemy do jednej głośności
        music_dict[x] = sample
    
    # dodajemy nutki do słownika
    samples_notes = np.unique(track_table[np.where(lengths == 3)])
    for x in samples_notes:
        if x == '---':
            continue
        sound = sound_sin(notes[x], (60 / bpm), 0, 0)
        note = np.repeat(sound, 2)
        note = np.reshape(note, (len(sound), 2))
        note = note / np.amax(note) # normujemy do jednej głośności
        music_dict[x] = note
        
    # dodajemy instrumenty do słownika
    sample_instruments = np.unique(track_table[np.where(lengths == 6)])
    global instrument
    for x in sample_instruments:
        if x == '------':
            continue
        instrument_file = open(dir + '/sample' + x[0:2] + '.txt', 'r')
        instrument_definition = instrument_file.read()
        instrument_file.close()
        exec(instrument_definition)
        instrument = instrument / np.amax(instrument) # normujemy do jednej głośności
        music_dict[x] = instrument
    
    # tworzymy ścieżkę
    fs = 44100 # częstotliwość
    delay = 0 # przesunięcie ze względu na wczytywane linie z samplami
    track = np.zeros((0,2))
    for line in track_table:
        for x in line:
            if (x != '--' and x != '---' and x != '------'):
                track = merge_sounds(track, music_dict[x], delay)
        delay += int((60 / bpm) * fs)

    # informacja z przesunięciem dla całej ścieżki
    track_delay = int(np.shape(track_table)[0] * (60 / bpm) * fs)
    
    return (track, track_delay)
