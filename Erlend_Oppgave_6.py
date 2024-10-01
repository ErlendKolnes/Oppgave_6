import  matplotlib.pyplot as plt


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
                    #return None
                    
                        
                    # Hent dato og tid fra første del
                    date_time = parts[0].split()
                    date = date_time[0]
                    time = date_time[1]
                        
                        # Hent andre målinger
                        #Sjekker om treje index er tom, hvis ikke gå til til else.
                    nr = parts[1]
                    trykk1 = parts[2].replace(',', '.')
                    trykk2 = parts[3].replace(',', '.')
                    temp = parts[4].replace(',', '.')

                    yield date, time, nr, trykk1, trykk2, temp
                
    except FileNotFoundError:
        print(f"Filen {r_data} ble ikke funnet.")
    except Exception as e:
        print(f"En feil oppstod: {e}")                   

    

# Initialiser lister for å lagre komponentene
r_dates = []
r_times = []
r_nrs = []
r_trykk1s = []
r_trykk2s = []
r_temps = []


r_fil = "trykk_og_temperaturlogg_rune_time.csv.txt"

#Linje nr som koden skal ignorere/hoppe over.
r_ignorer_linje = [1]
r_antall_tall = len(r_ignorer_linje)
#Antall linjer som skal brukes. Fra topp og nedover. 
r_antall_linje = 10 + r_antall_tall   


# Iterer over hver inn r_data streng og del den opp i komponenter
for date, time, nr, trykk1, trykk2, temp in r_split_string(r_fil, r_antall_linje, r_ignorer_linje):
    r_dates.append(date)
    r_times.append(time)
    r_nrs.append(nr)
    r_trykk1s.append(trykk1)
    r_trykk2s.append(trykk2)
    r_temps.append(temp)


x_verdier = r_nrs
y_verdier = r_trykk2s

plt.subplot(1, 1, 1)
plt.title("Oppgave 6")
plt.plot(x_verdier, y_verdier, linestyle = "dashed", marker = "x", label = "x i andre")


plt.xlabel("Tid")
plt.ylabel("Trykkmåliner")

plt.legend()
#olt.savefig("figuren.pdf")
plt.show()

r_fil.close()



if __name__ == "__main__":
    # Skriv ut resultatene
    print(f"Datoer: {r_dates}")
    print(f"Tider: {r_times}")
    print(f"r_nrs: {r_nrs}")
    print(f"r_trykk1s: {r_trykk1s}")
    print(f"r_trykk2s: {r_trykk2s}")
    print(f"Tempratur: {r_temps}")
