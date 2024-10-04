#Testfil for plotting fra forskjellige kodefiler

from sola_time import *

from gjennomsnitt_temp import *

import matplotlib.pyplot as plt

print(dt_liste)

plt.subplot(2, 1, 1)
plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
plt.plot(dt_liste, trykk2, label="Testtrykk", color="yellow")
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
plt.legend()

plt.show()