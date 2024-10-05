# Funksjon for å dele opp strengen i komponenter
import matplotlib.pyplot as plt
import datetime as d


def splitsolatime(data):

    # Del strengen ved semikolon
    s_parts = data.split(';')
    
    # Hent dato og tid
    s_date_time = s_parts[2].split()
    if len(s_date_time) != 0: #For å unngå feil ved "siste linje"
        s_date = s_date_time[0]
        s_time = s_date_time[1]

    # Hent trykk
    s_trykk_n = s_parts[4].replace(",", ".")
    fs_trykk = float(s_trykk_n) #Fjerner newline-tegn, gjør om til float-variabel
    s_trykk = (fs_trykk/10)

    # Hent tempertur
    s_temp_n = s_parts[3].replace(",", ".")
    s_temp = float(s_temp_n) #Gjør om til float-variabel
    
    return s_date, s_time, s_trykk, s_temp


#Åpner fil
fil_solatime = open("sola_time.csv.txt", "r", encoding="UTF8")


#Lager tomme lister til dato, tid, trykk og temp
s_dato_l = []
s_tid_l = []
s_trykk_l = []
s_temp_l = []


#Splitter opp data og sorterer i overnevnte lister
for linje in fil_solatime:
    if linje.split(";")[0] == "Sola":
        s_date, s_time, s_trykk, s_temp = splitsolatime(linje)
        s_dato_l.append(s_date)
        s_tid_l.append(s_time)
        s_trykk_l.append(s_trykk)
        s_temp_l.append(s_temp)


#Kode for å legge sammen dato og tid i en og samme liste
#s_dato_tid_l = []
# for i in range (len(s_dato_l)):
#     s_dato_tid_l.append(s_dato_l[i] + " " + s_tid_l[i])


#Gjør om dato og tidspunkt til egne lister
s_ny_dato = []
s_ny_tid = []
for i in range(len(s_dato_l)):
    s_ny_dato.append(s_dato_l[i].split("."))
    s_ny_tid.append(s_tid_l[i].split(":"))



#lage datetime-liste
s_dt_dato = []
for i in range(len(s_ny_dato)):
    dag = d.datetime(int(s_ny_dato[i][2]), int(s_ny_dato[i][1]), int(s_ny_dato[i][0]), int(s_ny_tid[i][0]), int(s_ny_tid[i][1]))
    s_dt_dato.append(dag)


#print(s_dt_dato)
#Testing av listene for å sjekke at ting stemmer
# print("Her er dato:", "\n", s_dato_l, "\n")
# print("Her er tid:", "\n", s_tid_l, "\n")
# print("Her er temp:", "\n", s_temp_l, "\n")
# print("Her er trykk:", "\n", s_trykk_l, "\n")
# print("Her er dato og tid sammen", "\n", s_dato_tid_l, "\n")

#Plotting (skjer ikke dersom programmet importeres til annet program)
if __name__ == "__main__":
    
    #Plotter graf for temp
    plt.subplot(2, 1, 1)
    plt.plot(s_dt_dato, s_temp_l, label="Temperatur MET", color="green")
    plt.legend()

    #Plotter graf for trykk
    plt.subplot(2, 1, 2)
    plt.plot(s_dt_dato, s_trykk_l, label="Absolutt trykk MET", color="green")
    plt.legend()

    #Lage riktig avstand mellom punktene (ikke nødvendig med datetime objekter)
    #plt.xticks(["11.06.2021 01:00", "12.06.2021 00:00", "13.06.2021 00:00", "14.06.2021 00:00"])
    #plt.yticks([10, 100, 500, 1000, 2000])

    #Vis grafene
    plt.show()


#Lukker fila
fil_solatime.close()