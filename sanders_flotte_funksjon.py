import datetime as d

def r_split_string(r_data, stop_line):
    try:
        with open(r_data, 'r') as r_fil:  # Use r_data parameter for file name
            r_data_linjer = r_fil.readlines()

            for linjenummer, linje in enumerate(r_data_linjer):
                if linjenummer < 12099:  # Skip lines until we reach line 12100
                    continue
                
                elif linjenummer > stop_line:  # Exit the loop if the line number exceeds the stop line
                    break

                else:
                    linje = linje.strip()

                    # Split the string by semicolon
                    parts = linje.split(';')
                    
                    if len(parts) < 5:
                        continue
                    
                    date_time_1 = parts[0].replace("/",".").replace(",",".")  # Extract date/time
                    nr = parts[1]            # Extract nr
                    trykk1 = parts[2].replace(',', '.')  # Extract trykk1
                    trykk2n = parts[3].replace(',', '.')  # Extract trykk2n
                    temp = parts[4].replace(',', '.')  # Extract temp

                    yield date_time_1, nr, trykk1, trykk2n, temp  # Yield all necessary values
                
    except FileNotFoundError:
        print(f"Filen {r_data} ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")     


stop_line = len()
r_fil = "rune_time.csv.txt"
rs_date_times = []  # Correct initialization

# Pass stop_line instead of r_antall_linje
for date_time, nr, trykk1, trykk2n, temp in r_split_string(r_fil, stop_line):
    rs_date_times.append(date_time)  # Append date_time

rs_ny_dato = []
rs_ny_tid=[]
rs_dato_1=[]



# Funksjon for å korrigere feil som '00:00' i 12-timers format
def korriger_tid_format(datoer):
    # Sjekk om tiden inneholder "00:00" med am/pm
    if "00:00" in datoer and ("am" in datoer.lower() or "pm" in datoer.lower()):
        # Erstatt med riktig representasjon av midnatt
        return datoer.replace("00:00", "12:00")
    return datoer

# Funksjon for å konvertere dato og tid til ønsket format
def konvertere_dato_tid(datoer):
    datoer = korriger_tid_format(datoer)
    try:
        return d.datetime.strptime(datoer, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datoer

# Example: splitting the third date-time entry into date and time
total_date_time = rs_date_times[2].split()




x=len(date_time)



# Check if both date and time exist after Splitting
if i in range(x)
    if len(total_date_time) >= 2:
        rs_date = total_date_time[0]  # First part is the date
        rs_time = total_date_time[1]  # Second part is the time
    else:
        rs_date = total_date_time[0]  # If no time is present, just assign the date
        rs_time = "00:00:00"  # Fallback for missing time

print(f"Date: {rs_date}, Time: {rs_time}")