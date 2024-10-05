

from sola_time import *
from gjennomsnitt_temp import *
import datetime as d
import matplotlib.pyplot as plt
import numpy as np

# Liste med tidspunkter (for eksempel)


# Start- og slutt-tidspunkter
start_tid = d.datetime(2021, 6, 11, 17, 31)
slutt_tid = d.datetime(2021, 6, 12, 3, 5)

# Finn indeksene til start og slutt
start_indeks = r_dates_times.index(start_tid)
slutt_indeks = r_dates_times.index(slutt_tid)

print(start_indeks)
print(slutt_indeks)

tid_hoy_lav_x = r_dates_times[start_indeks], r_dates_times[slutt_indeks]
temp_hoy_lav_y=r_temps[start_indeks], r_temps[slutt_indeks]

print(tid_hoy_lav_x)
print(temp_hoy_lav_y)




"""
plt.subplot(1,1,1)
plt.plot(r_dates_times, r_temps, marker='o')
#Tegn en rett linje mellom start og slutt
plt.plot(x,y, 'r--', label='Direkte linje')

# Formatering
plt.xlabel('Tid')
plt.ylabel('Verdi')
plt.legend()
plt.show()
"""