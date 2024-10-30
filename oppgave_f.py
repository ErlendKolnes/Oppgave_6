#oppgave_f

from samling_av_div import *

from rune_time import *

from math import *

"""
Liste for gjennomsnittsverdier temp hentet fra samling_av_div: snitt_temperaturer STARTER PÅ MÅLING 30, SLUTTER PÅ MÅLING -30
Tilsvarende liste for tidspunkter: gyldige_tidspunkter

Liste for temp maalinger hentet fra rune_time: r_temps
"""

liste_standardavvik = list() #lager tom liste for standardavvik

# For-løkke / funksjon for standardavvik, hver verdi legges til liste_standardavvik
for i in range(30, len(r_temps) - 30):
    summen = 0
    for a in range(60):
        summen += (r_temps[i - 30 + a] - snitt_temperaturer[i-30])**2
    liste_standardavvik.append(sqrt((1/(60-1)) * summen))
