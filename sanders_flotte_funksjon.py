import datetime as d
import matplotlib.pyplot as plt
from rune_time import *

def r_split_string(r_data, stop_line):
    try:
        with open(r_data, 'r') as r_fil:
            r_data_linjer = r_fil.readlines()

            for linjenummer, linje in enumerate(r_data_linjer):
                if linjenummer < 12099:  #12099 Skip lines until we reach line 12100
                    continue
                
                elif linjenummer > stop_line:  # Exit the loop if the line number exceeds the stop line
                    break

                else:
                    linje = linje.strip()

                    # Split the string by semicolon
                    parts = linje.split(';')
                    
                    if len(parts) < 5:
                        continue
                    
                    # Extract date/time
                    total_date_time = parts[0].split(" ")  # Split date and time
                    for_date = total_date_time[0]  # First part is the date
                    for_time = total_date_time[1]  # Second part is the time
                    
                    rs_date = for_date.replace("/", ".")  # Replace / with .
                    rs_time = for_time.replace(",", ".")  # Replace , with .

                    nr = parts[1]            
                    trykk1 = parts[2].replace(',', '.')  
                    trykk2n = parts[3].replace(',', '.')  
                    temp = parts[4].replace(',', '.')  

                    yield total_date_time, nr, trykk1, trykk2n, temp, total_date_time, rs_date, rs_time
                
    except FileNotFoundError:
        print(f"Filen {r_data} ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")     

stop_line = 22220  # Set the stop line

r_fil = "rune_time.csv.txt"
rs_date_times = []  # Correct initialization
rs_ny_dato = []
rs_ny_tid = []
temps = []

# Pass stop_line instead of r_antall_linje
for total_date_time, nr, trykk1, trykk2n, temp, date_time, date, time in r_split_string(r_fil, stop_line):
    rs_date_times.append(total_date_time)
    rs_ny_dato.append(date)
    rs_ny_tid.append(time)
    temps.append(float(temp))  # Convert temp to float and store it

# Convert date and time strings to datetime objects
rs_dtdato = []
for i in range(len(rs_ny_dato)):
    # Split the date and time strings into their components
    date_parts = rs_ny_dato[i].split('.')
    time_parts = rs_ny_tid[i].split(':')
    
    # Create a datetime object using the components
    dag = d.datetime(int(date_parts[2]), int(date_parts[0]), int(date_parts[1]), int(time_parts[0]), int(time_parts[1]), int(time_parts[2]))
    rs_dtdato.append(dag)

x = rs_dtdato
y = temps
#r_temps
#r_dates_times
# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Temperature')
plt.xlabel('Date and Time')
plt.ylabel('Temperature')
plt.title('Temperature over Time')
plt.legend()
plt.grid(True)
plt.show()


#rs_date = d.datetime.strftime("%d.%m.%Y")
#rs_time = d.datetime.strftime("%H:%M:%S")

#x=len(date_time)
#del rs_date_times[5]
#print(rs_dtdato)




# Check if both date and time exist after Splitting
#if i in range(x):
  #  if len(total_date_time) >= 2:
     #   rs_date = total_date_time[0]  # First part is the date
   #     rs_time = total_date_time[1]  # Second part is the time
   # else:
    #    rs_date = total_date_time[0]  # If no time is present, just assign the date
    #    rs_time = "00:00:00"  # Fallback for missing time

#print(f"Date: {rs_date}, Time: {rs_time}")


# Funksjon for å korrigere feil som '00:00' i 12-timers format
#def korriger_tid_format(datoer):
    # Sjekk om tiden inneholder "00:00" med am/pm
#    if "00:00" in datoer and ("am" in datoer.lower() or "pm" in datoer.lower()):
#        # Erstatt med riktig representasjon av midnatt
#        return datoer.replace("00:00", "12:00")
#    return datoer

# Funksjon for å konvertere dato og tid til ønsket format
#def konvertere_dato_tid(datoer):
#    datoer = korriger_tid_format(datoer)
#    try:
#        return d.datetime.strptime(datoer, "%Y-%m-%d %H:%M:%S")
#    except ValueError:
#        return datoer
