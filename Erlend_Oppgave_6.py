

import  matplotlib.pyplot as plt
from datetime import datetime


# Funksjon for å dele opp strengen i komponenter
def r_split_string(r_data, stop_line):
    try:
        with open(r_data, 'r') as r_fil:
            r_data_linjer = r_fil.readlines()

            for linjenummer, linje in enumerate(r_data_linjer, start=1):
                if linjenummer in [1]:
                    continue

                elif linjenummer > stop_line:
                    break                 
                else:
                    #linje = linje.strip()
                    linje = linje.strip()

                    # Del strengen ved semikolon
                    parts = linje.split(';')
                    
                    #if len(parts) < 5 or not parts[0] or not parts[1] or not parts[2] or not parts[3] or not parts[4]:
                    if len(parts) < 5:
                        continue
                    
                    #date_time = parts[0].split()
                    #if len(date_time) < 2:
                    #    print(f"Ugyldig dato/tid format på linje {linjenummer}: {parts[0]}")
                    #    continue
                        
                    # Hent dato og tid fra første del
                    #Splitter dato og tid i to lister
                    
                    date_time_1 = parts[0]
                    
                    date_time = konvertere_dato_tid(date_time_1)
                    #konvertere_dato_tid(date_time)  


                    # Hent andre målinger                    
                    nr = parts[1]

                    trykk1 = parts[2].replace(',', '.')
                    trykk2 = parts[3].replace(',', '.')
                    temp = parts[4].replace(',', '.')


                    

                    yield date_time, nr, trykk1, trykk2, temp
                
    except FileNotFoundError:
        print(f"Filen {r_data} ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")     



# Funksjon for å korrigere feil som '00:00' i 12-timers format
def korriger_tid_format(datoer):
    # Sjekk om tiden inneholder "00:00" med am/pm
    if "00:00" in datoer and "am" or "pm" in datoer.lower():
        # Erstatt med riktig representasjon av midnatt
        return datoer.replace("00:00", "12:00")
   
    return datoer



# Funksjon for å konvertere dato og tid til ønsket format
def konvertere_dato_tid(datoer):

    datoer = korriger_tid_format(datoer)
    #sekunder = konvertere_sekunder(sekunder)

    

    if "am" in datoer.lower() or "pm" in datoer.lower():     
        try:
            dt = datetime.strptime(datoer, "%m/%d/%Y %I:%M %p")
        except ValueError:
            return datoer
                
    else:
        try:   
            # Forsøk å analysere dato og tid i det første formatet (måned.dag.år timer:minutter)
            dt = datetime.strptime(datoer, "%m.%d.%Y %H:%M")
        except ValueError:
            return datoer
                  
                # Forsøk å analysere dato og tid i det andre formatet (måned/dag/år timer:minutter:sekunder am/pm)
              # Returner den opprinnelige strengen hvis analysen mislykkes
    
    # Returner den formaterte datoen og tiden (dag.måned.år timer:minutter:sekunder)
    return dt.strftime("%d.%m.%Y %H:%M")



def konvertere_sekunder(sekunder):
    #Bruker prosent 60 på alle tallene i listen for å få sekunder
    for i in range(len(sekunder)):
        sekunder[i] = int(sekunder[i]) % 60
    
    return sekunder
        


def kobinere_tider(tider, sekunder):
    nye_tider = []
    for tid, sek in zip(tider, sekunder):
        time, minutt = map(int, tid.split(':'))
        ny_tid = f"{time:02}:{minutt:02}:{sek:02}"
        nye_tider.append(ny_tid)
    return nye_tider


#>Fyller inn verider for barometrisk trykk
#LEgger inn det den sist index veriden som den har lest
def fylle_inn_verdier_b_trykk(b_trykk):
    teller = 0
    for element in b_trykk:
        if element == '':
            b_trykk[teller] = b_trykk[teller-1]
        teller += 1




# Initialiser lister for å lagre komponentene
# dag.måned.år timer:minutter
r_dates_times = []
# timer:minutter
r_times = []
# nr/sekunder
r_nrs = []
#Barometrisk trykk
r_trykk_b = []
#Absolutt trykk
r_trykk_a = []
#Tempratur
r_temps = []       



r_fil = ("Oving/Oving_6/trykk_og_temperaturlogg_rune_time.csv.txt")



#Linje nr som koden skal ignorere/hoppe over.

#Antall linjer som skal brukes. Fra topp og nedover. 
r_antall_linje = float('inf')



print (f"Antall linjer {r_antall_linje}")

for date_time, nr, trykk1, trykk2, temp in r_split_string(r_fil, r_antall_linje):
    r_dates_times.append(date_time)
    r_nrs.append(nr)
    r_trykk_b.append(trykk1)
    r_trykk_a.append(trykk2)
    r_temps.append(temp)



antall_temp_maalinger = len(r_temps)
fylle_inn_verdier_b_trykk(r_trykk_b)



if __name__ == "__main__":
    # Skriv ut resultatene
    print(f"Dato og tid: {r_dates_times}")
    print(f"Sekunder: {r_nrs}")
    print(f"r_trykk_b: {r_trykk_b}")
    print(f"r_trykk_a: {r_trykk_a}")
    print(f"Tempratur: {r_temps}")
    print(f"Antall temp maalinger: {antall_temp_maalinger}")