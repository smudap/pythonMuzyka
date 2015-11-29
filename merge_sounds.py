# -*- coding: utf-8 -*-

import numpy as np

"""
Moduł z funkcją do złączania dwóch dźwięków
stosując przesunięcie dźwięków w ścieżce.
"""

print('Modul o nazwie: ' + __name__ + ' zostal wczytany.')

def merge_sounds(sound1, sound2, delay):
    
    """
    Funkcja złączająca dwa dźwięki.
    Argumenty:
        * sound1 - dźwięk pierwszy
        * sound2 - dźwięk drugi
        * delay - przesunięcie określające, która linia ścieżki zostaje wczytana
    """
    
    # sprawdzamy długości dzwięków, bo muszą być równej
    # długości by je złączyć (dodawanie macierzy wymiaru
    # n x 2)
    lines_sound1 = np.shape(sound1)[0]
    lines_sound2 = np.shape(sound2)[0]
    
    # łączymy dzwięki korygując wymiary macierzy
    delay_matrix1 = np.zeros((delay, 2))
    if lines_sound1 >= lines_sound2 + delay:
        delay_matrix2 = np.zeros((lines_sound1 - (delay + lines_sound2), 2))
        sound = sound1 + np.vstack((delay_matrix1, sound2, delay_matrix2))
    else:
        delay_matrix3 = np.zeros(((delay + lines_sound2) - lines_sound1, 2))
        sound = np.vstack((sound1, delay_matrix3)) + np.vstack((delay_matrix1, sound2))
                
    return sound