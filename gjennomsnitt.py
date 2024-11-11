'''e) Programmet deres skal finne gjennomsnittlig forskjell mellom temperatur og trykk de to
dataseriene (Rune Time datasettet og det fra Meteorologisk institutt) samt hvilke
tidspunkter forskjellen mellom de to seriene er lavest og høyest. Dere trenger bare å
sammenlikne de linjene i hver fil der tidspunktene er like (for hver dag og time i den ene
fila, finn tilsvarende dag og time med 0 minutter i den andre fila)'''

import datetime as d
import pandas as pd


from sola_time import *
from rune_time import *



#Filtrerer ut tidspunktene som har 00 minutter
r_filtrer_verdier = [i for i, ts in enumerate(r_dates_times) if ts.minute == 0 and  ts.second < 10]


#Filtrerer ut trykk og temp verdiene som har 00 minutter
r_filtrert_dates_times = [r_dates_times[i] for i in r_filtrer_verdier]
r_filtrert_temps = [r_temps[i] for i in r_filtrer_verdier]
r_filtrert_trykk_a = [r_trykk_a[i] for i in r_filtrer_verdier]

'''
if __name__ == "__main__":
    print("Antall datoer: ", len(r_filtrert_dates_times))
    print("Antall temperaturer: ", len(r_filtrert_temps))
    print("Antall trykk_a: ", len(r_filtrert_trykk_a))
    print("filtrert dates times: ", r_filtrert_dates_times)
    print("filtrert temps: ", r_filtrert_temps)
    print("filtrert trykk_a: ", r_filtrert_trykk_a)

'''
#Lager dataframes fra listenene med tidspunkt og verdier
rune_time_df = pd.DataFrame({
    'timestamp': r_filtrert_dates_times,
    'temprature': r_filtrert_temps,
    'presure': r_filtrert_trykk_a
})

met_inst_def = pd.DataFrame({
    'timestamp': s_dt_dato,
    'temprature': s_temp_l,
    'presure': s_trykk_l
})


#Slår sammen datserien basert på tidsstemplene
merged_df = pd.merge(rune_time_df, met_inst_def, on='timestamp', suffixes = ('_rune', '_met'))

#Beregn forskjellen mellom temperaturene og trykkene
merged_df['temp_diff'] = merged_df['temprature_rune'] - merged_df['temprature_met']
merged_df['pres_diff'] = merged_df['presure_rune'] - merged_df['presure_met']

#Beregn gjennomsnittet av forskjellene
avg_temp_diff = merged_df['temp_diff'].abs().mean()
avg_pres_diff = merged_df['pres_diff'].abs().mean()

#Finn tidspunkt med lavest og høyest forskjell
lavest_temp_diff_timestamp = merged_df.loc[merged_df['temp_diff'].idxmin()]['timestamp']
høyest_temp_diff_timestamp = merged_df.loc[merged_df['temp_diff'].idxmax()]['timestamp']
lavest_pressure_diff_timestamp = merged_df.loc[merged_df['pres_diff'].idxmin()]['timestamp']
høyest_pressure_diff_timestamp = merged_df.loc[merged_df['pres_diff'].idxmax()]['timestamp']


if __name__ == "__main__":
    print("DataFrame: ", merged_df)
    print("Gjennomsnittlig temperaturforskjell: ", avg_temp_diff)
    print("Gjennomsnittlig trykkforskjell: ", avg_pres_diff)
    print("Tidspunkt med lavest temperaturforskjell: ", lavest_temp_diff_timestamp)
    print("Tidspunkt med høyest temperaturforskjell: ", høyest_temp_diff_timestamp)
    print("Tidspunkt med lavest trykkforskjell: ", lavest_pressure_diff_timestamp)
    print("Tidspunkt med høyest trykkforskjell: ", høyest_pressure_diff_timestamp)

