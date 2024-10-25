from sola_time import *
from gjennomsnitt_temp import *
import datetime as d
import matplotlib.pyplot as plt
import numpy as np


# Start- og slutt-tidspunkter
start_tid = d.datetime(2021, 6, 11, 17, 31)
slutt_tid = d.datetime(2021, 6, 12, 3, 5)

start_tid_s=d.datetime(2021,6,11,17,00)
slutt_tid_s=d.datetime(2021, 6, 12, 3, 0)

#  indeksene til start og slutt
start_indeks_r = r_dates_times.index(start_tid)
slutt_indeks_r = r_dates_times.index(slutt_tid)

start_indeks_s=s_dt_dato.index(start_tid_s)
slutt_indeks_s=s_dt_dato.index(slutt_tid_s)

tid_hoy_lav_x_r = r_dates_times[start_indeks_r], r_dates_times[slutt_indeks_r]
temp_hoy_lav_y_r=r_temps[start_indeks_r], r_temps[slutt_indeks_r]

tid_hoy_lav_x_s = s_dt_dato[start_indeks_s],s_dt_dato[slutt_indeks_s]
temp_hoy_lav_y_s = s_temp_l[start_indeks_s],s_temp_l[slutt_indeks_s]

if __name__ == "__main__":
    print(start_indeks_r)
    print(slutt_indeks_r)
    print(tid_hoy_lav_x_r)
    print(temp_hoy_lav_y_r)




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

