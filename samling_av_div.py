from sola_time import *
from gjennomsnitt_temp import *
import datetime as d
import matplotlib.pyplot as plt
import numpy as np


# Start- og slutt-tidspunkter
start_tid = d.datetime(2021, 6, 11, 17, 31)
slutt_tid = d.datetime(2021, 6, 12, 3, 5)

#  indeksene til start og slutt
start_indeks = r_dates_times.index(start_tid)
slutt_indeks = r_dates_times.index(slutt_tid)

tid_hoy_lav_x = r_dates_times[start_indeks], r_dates_times[slutt_indeks]
temp_hoy_lav_y=r_temps[start_indeks], r_temps[slutt_indeks]

if __name__ == "__main__":
    print(start_indeks)
    print(slutt_indeks)
    print(tid_hoy_lav_x)
    print(temp_hoy_lav_y)




def gjennommsnitt_temp(tider, temperaturer, n):
    gyldige_tidspunkter = []
    snitt_temperaturer = []
    
    # Looper gjennom temperaturene 
    for i in range(n, len(temperaturer) - n):
        utvalg = temperaturer[i - n:i + n + 1]
        gjennomsnitt = sum(utvalg) / len(utvalg)
        
        gyldige_tidspunkter.append(tider[i])
        snitt_temperaturer.append(gjennomsnitt)
    
    return gyldige_tidspunkter, snitt_temperaturer


tider = r_dates_times
gyldige_tidspunkter, snitt_temperaturer = gjennommsnitt_temp(tider, r_temps, 30)


if __name__ == "__main__":
    print("Gydlige tidspunkter er: ",gyldige_tidspunkter)
    print("snitt temperatur er: ",snitt_temperaturer)

