import matplotlib.pyplot as plt
import pandas as pd

from sola_time import *
from rune_time import *
from samling_av_div import *
from sinnes_time import *
from sauda_time import *
from oppgave_f import *
from gjennomsnitt import *


#Print må stå her for å printe får grafene kommer opp :)
print(f"Gjennomsnittlig temperaturforskjell: { avg_temp_diff:.2f}")
print(f"Gjennomsnittlig trykkforskjell: {avg_pres_diff:.2f}")
print(f"Tidspunkt med lavest temperaturforskjell: ", lavest_temp_diff, "Rune Temp:", r_lavest_temp_diff, "Met Temp:", met_lavest_temp_diff,
        f"Temp Diff: {abs(r_lavest_temp_diff - met_lavest_temp_diff):.2f}")
print(f"Tidspunkt med høyest temperaturforskjell: ", høyest_temp_diff, "Rune Temp:", r_høyest_temp_diff, "Met Temp:", met_høyest_temp_diff, 
        f"Temp Diff: {abs(r_høyest_temp_diff - met_høyest_temp_diff):.2f}")
print(f"Tidspunkt med lavest trykkforskjell: ", lavest_pressure_diff, "Rune Pressure:", r_lavest_pressure_diff, "Met Pressure:", met_lavest_pressure_diff, 
        f"Pressure Diff: {abs(r_lavest_pressure_diff - met_lavest_pressure_diff):.2f}")
print("Tidspunkt med høyest trykkforskjell: ", høyest_pressure_diff , "Rune Pressure:", r_høyest_pressure_diff, "Met Pressure:", met_høyest_pressure_diff, 
        f"Pressure Diff: {abs(r_høyest_pressure_diff - met_høyest_pressure_diff):.2f}")



plt.subplot(2,1, 1)
plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
plt.plot(r_dates_times, r_temps, label="Temperatur", color="blue")
# plt.plot(gyldige_tidspunkter, snitt_temperaturer, label='Gjennomsnittstemperatur', color='orange')
plt.errorbar(gyldige_tidspunkter, snitt_temperaturer, yerr=liste_standardavvik, errorevery=30, label="Gjennomsnittstemperatur", color="orange")
plt.plot(tid_hoy_lav_x, temp_hoy_lav_y, label='Høyeste og laveste temperatur', color='purple')
plt.plot(si_dt_dato, si_temp_l, label="Temperatur Sinnes", color="red")
plt.plot(sau_dt_dato, sau_temp_l, label="Temperatur Sauda", color="yellow")
plt.scatter(lavest_temp_diff, r_lavest_temp_diff , marker = "o", color='Red', label='Lavest Temp Diff')
plt.scatter(lavest_temp_diff, met_lavest_temp_diff, marker = "o", color='Red')
plt.scatter(høyest_temp_diff, r_høyest_temp_diff, marker = "x", color='Red', label='Høyest Temp Diff')
plt.scatter(høyest_temp_diff, met_høyest_temp_diff, marker = "x", color='Red')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
plt.plot(r_dates_times, r_trykk_a, label="Absolutt trykk", color="blue")
plt.plot(r_dates_times, r_trykk_b, label="Barometrisk trykk", color="orange")
plt.plot(si_dt_dato, si_trykk_l, label="Trykk Sinnes", color="red")
plt.plot(sau_dt_dato, sau_trykk_l, label="Trykk Sauda", color="yellow")
plt.scatter(lavest_pressure_diff, r_lavest_pressure_diff, marker="o", color='Red', label='Lavest Pressure Diff')
plt.scatter(lavest_pressure_diff, met_lavest_pressure_diff, marker="o", color='Red')
plt.scatter(høyest_pressure_diff, r_høyest_pressure_diff, marker="x", color='Red', label='Høyest Pressure Diff')
plt.scatter(høyest_pressure_diff, met_høyest_pressure_diff, marker="x", color='Red')
plt.grid(True)
plt.legend()



plt.show()


