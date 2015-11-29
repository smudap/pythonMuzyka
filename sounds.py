# -*- coding: utf-8 -*-

import numpy as np
import scipy.signal as scs

"""
Moduł z definicją dźwięków.
"""

print('Modul o nazwie: ' + __name__ + ' zostal wczytany.')

def sound_sin(f, t, a, d):
    
    """
    Funkcja tworząca falę sinusoidalną.
    Argumenty:
        * f - częstotliwość dźwięku
        * t - czas trwania dźwięku
        * a - czas trwania attack
        * d - czas trwania decay
    """
    
    # tworzymy falę
    f_s = 44100
    t0 = np.linspace(0, t, t * f_s)
    wave = np.sin(2 * np.pi * f * t0)
    
    # tworzymy attack
    A = np.floor(a * t * f_s)
    attack = np.linspace(0, 1, A)
    
    # tworzymy decay
    D = np.floor(d * t * f_s)
    decay = np.linspace(1, 0, D)
    
    # tworzymy sustain
    sustain = np.ones(t * f_s - A - D)
    
    # złączamy dzwięki
    sound = np.hstack((attack, sustain, decay)) * wave
    
    return sound
    
def sound_sawtooth(f, t, a, d):
    
    """
    Funkcja tworząca falę trójkątną (piła).
    Argumenty:
        * f - częstotliwość dźwięku
        * t - czas trwania dźwięku
        * a - czas trwania attack
        * d - czas trwania decay
    """
    
    # tworzymy falę
    f_s = 44100
    t0 = np.linspace(0, t, t * f_s)
    wave = scs.sawtooth(2 * np.pi * f * t0)
    
    # tworzymy attack
    A = np.floor(a * t * f_s)
    attack = np.linspace(0, 1, A)
    
    # tworzymy decay
    D = np.floor(d * t * f_s)
    decay = np.linspace(1, 0, D)
    
    # tworzymy sustain
    sustain = np.ones(t * f_s - A - D)
    
    # złączamy dzwięki
    sound = np.hstack((attack, sustain, decay)) * wave
    
    return sound
    
def sound_rectangle(f, t, a, d):
    
    """
    Funkcja tworząca falę prostokątną.
    Argumenty:
        * f - częstotliwość dźwięku
        * t - czas trwania dźwięku
        * a - czas trwania attack
        * d - czas trwania decay
    """
    
    # tworzymy falę
    f_s = 44100
    t0 = np.linspace(0, t, t * f_s)
    wave = np.sign(np.sin(2 * np.pi * f * t0))
    
    # tworzymy attack
    A = np.floor(a * t * f_s)
    attack = np.linspace(0, 1, A)
    
    # tworzymy decay
    D = np.floor(d * t * f_s)
    decay = np.linspace(1, 0, D)
    
    # tworzymy sustain
    sustain = np.ones(t * f_s - A - D)
    
    # złączamy dzwięki
    sound = np.hstack((attack, sustain, decay)) * wave
    
    return sound