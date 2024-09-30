
# Funksjon for å dele opp strengen i komponenter
def split_string(data):
    #parts = data.replace(';;', ';')


    # Del strengen ved semikolon
    parts = data.split(';')
    
    #if len(parts) < 5 or not parts[0] or not parts[1] or not parts[2] or not parts[3] or not parts[4]:
        
        #return None

    # Hent dato og tid fra første del
    date_time = parts[0].split()
    date = date_time[0]
    time = date_time[1]
    
    # Hent andre målinger
    nr = parts[1]
    trykk1 = parts[2].replace(',', '.')
    trykk2 = parts[3].replace(',', '.')
    temp = parts[4].replace(',', '.')
    
    return date, time, nr, trykk1, trykk2, temp



fil = open("Oving/Oving_6/trykk_og_temperaturlogg_rune_time.csv.txt", 'r', encoding = "UTF8" )


# Initialiser lister for å lagre komponentene
dates = []
times = []
nrs = []
trykk1s = []
trykk2s = []
temps = []

# Iterer over hver inndata streng og del den opp i komponenter
for fil in fil:
    date, time, nr, trykk1, trykk2, temp = split_string(fil)
    dates.append(date)
    times.append(time)
    nrs.append(nr)
    trykk1s.append(trykk1)
    trykk2s.append(trykk2)
    temps.append(temp)

# Skriv ut resultatene
print(f"Datoer: {dates}")
print(f"Tider: {times}")
print(f"NRs: {nrs}")
print(f"Trykk1s: {trykk1s}")
print(f"Trykk2s: {trykk2s}")
print(f"Tempratur: {temps}")

