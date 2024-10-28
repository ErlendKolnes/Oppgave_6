import matplotlib.pyplot as plt
import datetime as d

from sola_time import *
from rune_time import *
from samling_av_div import *


plt.subplot(4, 1, 1)
plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
plt.plot(r_dates_times, r_temps, label="Temperatur", color="blue")
plt.plot(gyldige_tidspunkter, snitt_temperaturer, label='Gjennomsnittstemperatur', color='orange')
plt.plot(tid_hoy_lav_x_r, temp_hoy_lav_y_r, label='Høyeste og laveste temperatur', color='purple')
plt.plot(tid_hoy_lav_x_s, temp_hoy_lav_y_s, label='Høyeste og laveste temperatur MET', color='red')
plt.legend()

#test_x = r_dates_times+rs_dtdato

plt.subplot(2, 1, 2)
plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
plt.plot(r_dates_times, r_trykk_a, label="Absolutt trykk", color="blue")
plt.plot(r_dates_times, r_trykk_b, label="Barometrisk trykk", color="orange")
plt.legend()


plt.show()







min_temp = min(min(s_temp_l), min(r_temps))
max_temp = max(max(s_temp_l), max(r_temps))

# Bruker 'bins' til å dekke hele grad-intervaller
plt.subplot(2, 1, 1)
plt.hist(s_temp_l, bins=range(int(min_temp), int(max_temp) + 1), edgecolor='black', label='Temperatur MET', color='blue')
plt.xlabel('Temperatur C')
plt.ylabel('Frekvens')
plt.title('Histogram for Temperatur MET')
plt.legend(['Temperatur MET'])

plt.subplot(2, 1, 2)
plt.hist(r_temps, bins=range(int(min_temp), int(max_temp) + 1), edgecolor='red', label='Temperatur r',color='green')
plt.xlabel('Temperatur C')
plt.ylabel('Frekvens')
plt.title('Histogram av Temperaturer fra Begge Filer')
plt.legend(['Temperatur r'])

# Viser plottet
plt.show()

#print(r_dates_times)

#print(s_dt_dato)

plt.show()