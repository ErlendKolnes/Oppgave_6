
from sola_time import *
from rune_time import *
import datetime as d
import matplotlib.pyplot as plt
import numpy as np

min_temp = min(min(s_temp_l), min(r_temps))
max_temp = max(max(s_temp_l), max(r_temps))


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



trykk_differanse = [a - b for a, b in zip(r_trykk_a, r_trykk_b) ]


def G_gjennomsnitt(data, n=10):
    Glattet_trykk = []
    for i in range(len(data)):
        start = max(0, i - n)
        end = min(len(data), i + n + 1)
        gjennomsnitt = np.mean(data[start:end])
        Glattet_trykk.append(gjennomsnitt)
    return Glattet_trykk


Trykk_diff_g = G_gjennomsnitt(trykk_differanse, n=10)

if __name__ == "__main__":
    #print(Trykk_diff_g)
    plt.figure(figsize=(12, 6))
    plt.plot(r_dates_times[:len(trykk_differanse)], trykk_differanse, label='Trykkdifferanse', color='blue')
    plt.plot(r_dates_times[:len(Trykk_diff_g)], Trykk_diff_g, label='Trykk_diff_g', color='orange')
    plt.xlabel('Tidspunkt')
    plt.ylabel('Differanse (Absolutt - Barometrisk trykk)')
    plt.title('Differanse mellom Absolutt og Barometrisk Trykk ')
    plt.legend()
    plt.show()
