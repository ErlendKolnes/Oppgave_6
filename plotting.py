import matplotlib.pyplot as plt
#import datetime as d

from sola_time import *
from rune_time import *
from sanders_flotte_funksjon import *

plt.subplot(2, 1, 1)
#plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
plt.plot(r_dates_times, r_temps, label="Temperatur", color="blue")
plt.legend()
test_x = r_dates_times+rs_dtdato
plt.subplot(2, 1, 2)
#plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
plt.plot(test_x, r_trykk_a, label="Absolutt trykk", color="blue")
plt.plot(test, r_trykk_b, label="Barometrisk trykk", color="orange")
plt.legend()

#print(r_dates_times)

#print(s_dt_dato)

plt.show()