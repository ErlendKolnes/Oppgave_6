'''e) Programmet deres skal finne gjennomsnittlig forskjell mellom temperatur og trykk de to
dataseriene (Rune Time datasettet og det fra Meteorologisk institutt) samt hvilke
tidspunkter forskjellen mellom de to seriene er lavest og høyest. Dere trenger bare å
sammenlikne de linjene i hver fil der tidspunktene er like (for hver dag og time i den ene
fila, finn tilsvarende dag og time med 0 minutter i den andre fila)'''

#Last ned pandas med å skrive pip: install pandas i terminalen
import pandas as pd

from sola_time import *
from rune_time import *



#Filtrerer ut tidspunktene som har 00 minutter
r_filtrer_verdier = [i for i, ts in enumerate(r_dates_times) if ts.minute == 0 and  ts.second < 10]


#Filtrerer ut trykk og temp verdiene som har 00 minutter
r_filtrert_dates_times = [r_dates_times[i] for i in r_filtrer_verdier]
r_filtrert_temps = [r_temps[i] for i in r_filtrer_verdier]
r_filtrert_trykk_a = [r_trykk_a[i] for i in r_filtrer_verdier]

#Filtrerer ut tidspunktene som har 00 minutter, feilsøking
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
merged_df['temp_diff'] = (merged_df['temprature_rune'] - merged_df['temprature_met']).abs()
merged_df['pres_diff'] = (merged_df['presure_rune'] - merged_df['presure_met']).abs()

#Beregn gjennomsnittet av forskjellene
avg_temp_diff = merged_df['temp_diff'].mean()
avg_pres_diff = merged_df['pres_diff'].mean()

'''
# Finn de to laveste og høyeste temperaturforskjellene
lavest_temp_diff = merged_df.nsmallest(2, 'temp_diff')
høyest_temp_diff = merged_df.nlargest(2, 'temp_diff')

# Finn de to laveste og høyeste trykkforskjellene
lavest_pressure_diff = merged_df.nsmallest(2, 'pres_diff')
høyest_pressure_diff = merged_df.nlargest(2, 'pres_diff')

'''
#Finner de to tidspunktene med lavest og høyest temperaturforskjell
lavest_temp_diff = merged_df.loc[merged_df['temp_diff'].idxmin()]['timestamp']
høyest_temp_diff = merged_df.loc[merged_df['temp_diff'].idxmax()]['timestamp']

#Finner de to tidspunktene med lavest og høyest trykkforskjell
lavest_pressure_diff = merged_df.loc[merged_df['pres_diff'].idxmin()]['timestamp']
høyest_pressure_diff = merged_df.loc[merged_df['pres_diff'].idxmax()]['timestamp']

# Hent råverdiene for de tidspunktene med lavest og høyest temperaturforskjell
r_lavest_temp_diff = rune_time_df.at[rune_time_df[rune_time_df['timestamp'] == lavest_temp_diff].index[0], 'temprature']
r_høyest_temp_diff = rune_time_df.at[rune_time_df[rune_time_df['timestamp'] == høyest_temp_diff].index[0], 'temprature']

met_høyest_temp_diff = met_inst_def.at[met_inst_def[met_inst_def['timestamp'] == høyest_temp_diff].index[0], 'temprature']
met_lavest_temp_diff = met_inst_def.at[met_inst_def[met_inst_def['timestamp'] == lavest_temp_diff].index[0], 'temprature']

r_høyest_pressure_diff = rune_time_df.at[rune_time_df[rune_time_df['timestamp'] == høyest_pressure_diff].index[0], 'presure']
r_lavest_pressure_diff = rune_time_df.at[rune_time_df[rune_time_df['timestamp'] == lavest_pressure_diff].index[0], 'presure']

met_høyest_pressure_diff = met_inst_def.at[met_inst_def[met_inst_def['timestamp'] == høyest_pressure_diff].index[0], 'presure']
met_lavest_pressure_diff = met_inst_def.at[met_inst_def[met_inst_def['timestamp'] == lavest_pressure_diff].index[0], 'presure']

if __name__ == "__main__":
    print("DataFrame:", merged_df)
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
    


'''
# Hente ut verdien i rad 5, kolonne 'temperature'
temp_value = df.at[5, 'temperature']

# Hente ut verdien i rad med indeks '2024-11-11 17:00:00', kolonne 'pressure'
pressure_value = df.at['2024-11-11 17:00:00', 'pressure']
   '''
