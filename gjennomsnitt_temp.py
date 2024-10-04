import matplotlib.pyplot as plt
import numpy as np

from sola_time import *
from rune_time import *

import matplotlib.pyplot as plt

def gjennommsnitt_temp(tider, temperaturer, n):
    gyldige_tidspunkter = []
    snitt_temperaturer = []
    
    # Looper gjennom temperaturene 
    for i in range(n, len(temperaturer) - n):
        # Hent de n forrige, den nåværende, og de n neste målingene
        utvalg = temperaturer[i - n:i + n + 1]
        gjennomsnitt = sum(utvalg) / len(utvalg)
        
        # Legger til gyldig tidspunkt og gjennomsnittsverdien
        gyldige_tidspunkter.append(tider[i])
        snitt_temperaturer.append(gjennomsnitt)
    
    return gyldige_tidspunkter, snitt_temperaturer

# Eksempel bruk av funksjonen
tider = r_dates_times
# Kaller funksjonen med n=30
gyldige_tidspunkter, snitt_temperaturer = gjennommsnitt_temp(tider, r_temps, 30)


