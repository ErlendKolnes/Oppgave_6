import matplotlib.pyplot as plt
import datetime as d

from sola_time import *
from rune_time import *
#from sanders_flotte_funksjon import *
from gjennomsnitt_temp import *
from Testfil import *


plt.subplot(4, 1, 1)
plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
plt.plot(r_dates_times, r_temps, label="Temperatur", color="blue")
plt.plot(gyldige_tidspunkter, snitt_temperaturer, label='Gjennomsnittstemperatur', color='orange')
plt.plot(tid_hoy_lav_x, temp_hoy_lav_y, label='Høyeste og laveste temperatur', color='purple')
plt.legend()

#test_x = r_dates_times+rs_dtdato

plt.subplot(2, 1, 2)
plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
plt.plot(r_dates_times, r_trykk_a, label="Absolutt trykk", color="blue")
plt.plot(r_dates_times, r_trykk_b, label="Barometrisk trykk", color="orange")
plt.legend()

#print(r_dates_times)

#print(s_dt_dato)

plt.show()