
#Erlend sitt tull




'''
def get_value():
    return 42

result = get_value()
print(result)  # Output: 42
'''

'''
def generate_values():
    yield 1
    yield 2
    yield 3

for value in generate_values():
    print(value)
# Output:
# 1
# 2
# 3
# 

 '''



import  matplotlib.pyplot as plt
import datetime as dt


# Funksjon for å dele opp strengen i komponenter
def r_split_string(r_data, stop_line, r_ignorer_linje):
    try:
        with open(r_data, 'r') as r_fil:
            r_data_linjer = r_fil.readlines()

            for linjenummer, linje in enumerate(r_data_linjer, start=1):
                if linjenummer in r_ignorer_linje:
                    continue

                elif linjenummer > stop_line:
                    break                 
                else:
                    linje = linje.strip()

                    # Del strengen ved semikolon
                    parts = linje.split(';')
                    
                    #if len(parts) < 5 or not parts[0] or not parts[1] or not parts[2] or not parts[3] or not parts[4]:
                    if len(parts) < 5:
                        continue
                    
                    
                        
                    # Hent dato og tid fra første del
                    #Splitter dato og tid i to lister
                    date_time = parts[0].split()
                    date = date_time[0]
                    time = date_time[1]
                        
                    # Hent andre målinger                    
                    nr = parts[1]
                    trykk1 = parts[2].replace(',', '.')
                    trykk2 = parts[3].replace(',', '.')
                    temp = parts[4].replace(',', '.')

                    yield date, time, nr, trykk1, trykk2, temp
                
    except FileNotFoundError:
        print(f"Filen {r_data} ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")                   

    

def konvertere_datoformat(datoer):
    # Konverterer strengen til en datetime-objekt
    # Konverterer datetime-objektet tilbake til en streng i ønsket format
    return [dt.datetime.strptime(dato, "%m.%d.%Y").strftime("%d.%m.%Y") for dato in datoer]
    


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


def kobinere_dato_og_tider (datoer, tider):
    kombinert = []
    for dato, tid in zip(datoer, tider):
        kombinert.append (f"{dato} {tid}")
        
    return kombinert

# Initialiser lister for å lagre komponentene
# måned.dag.år
r_dates = []
# dag.måned.år
r_dates_k = []
# timer:minutter
r_times = []
# nr
r_nrs = []
# sekduner
r_nrs_k = []
# timer:minutter:sekunder
r_tider_k = []
# dag.måned.år timer:minutter:sekunder
r_dato_tider_k = []

r_trykk_b = []
r_trykk_a = []
r_temps = []


r_fil = ("Oving/Oving_6/trykk_og_temperaturlogg_rune_time.csv.txt")


#Endrer back-slah til front-slah i filen
#r_fil = r_filstil.replace("\\t", "/")
#r_fil = r_filstil.replace("\\", "/")



#Linje nr som koden skal ignorere/hoppe over.
r_ignorer_linje = [1, 20223]
r_antall_tall = len(r_ignorer_linje)
#Antall linjer som skal brukes. Fra topp og nedover. 
r_antall_linje = 5 + r_antall_tall   


# Iterer over hver inn r_data streng og del den opp i komponenter
for date, time, nr, trykk1, trykk2, temp in r_split_string(r_fil, r_antall_linje, r_ignorer_linje):
    r_dates.append(date)
    r_times.append(time)
    r_nrs.append(nr)
    r_trykk_b.append(trykk1)
    r_trykk_a.append(trykk2)
    r_temps.append(temp)


#konventer dato formate fra måned.dag til dag.måned
r_dates_k = konvertere_datoformat(r_dates)
konvertere_sekunder(r_nrs)
r_tider_k = kobinere_tider(r_times, r_nrs)
r_dato_tider_k = kobinere_dato_og_tider(r_dates_k, r_tider_k)



#matlab, lager grafer and shit
x_verdier_1 = r_nrs
x_verdier_2 = r_times
y_verdier_1 = r_trykk_b
y_verdier_2 = r_trykk_a
y_verdier_3 = r_temps


'''
plt.subplot(1, 1, 1)
plt.title("Oppgave 6")
plt.plot(x_verdier_2, y_verdier_2, linestyle = "dashed", marker = "x", label = "Trykk-Barometer", color = "orange");
plt.plot(x_verdier_1, y_verdier_1, linestyle = "dashed", marker = "x", label = "Absloutt trykk", color = "blue" )

#plt.plot(x_verdier, y_verdier, linestyle = "dashed", marker = "x", label = "x i andre")


plt.xlabel("Tid")
plt.ylabel("Trykkmåliner")

plt.legend()
#plt.savefig("figuren.pdf")
plt.show()


'''

if __name__ == "__main__":
    # Skriv ut resultatene
    print(f"Dato og tid: {r_dato_tider_k}")
    print(f"Datoer: {r_dates}")
    print(f"Konvertert datoer: {r_dates_k}")
    print(f"Tider: {r_times}")
    print(f"Sekunder: {r_nrs}")
    print(f"Tider og sekunder: {r_tider_k}")
    print(f"Konvertert til sekunder: {r_nrs_k}")
    print(f"r_trykk_b: {r_trykk_b}")
    print(f"r_trykk_a: {r_trykk_a}")
    print(f"Tempratur: {r_temps}")
    
