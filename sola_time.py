# Funksjon for å dele opp strengen i komponenter
import matplotlib.pyplot as plt
import datetime as d

def splitsolatime(data):

    

    # Del strengen ved semikolon
    s_parts = data.split(';')
    
    

    # Hent dato og tid fra første del
    s_date_time = s_parts[2].split()
    if len(s_date_time) != 0:
        s_date = s_date_time[0]
        s_time = s_date_time[1]
        
    # Hent andre målinger

    s_trykk_n = s_parts[4].replace(",", ".")
    s_trykk_n = s_parts[4].split()
    s_trykk = s_trykk_n[0]

    s_temp = s_parts[3].replace(",", ".")
    
    return s_date, s_time, s_trykk, s_temp




fil_solatime = open("sola_time.csv.txt", "r", encoding="UTF8")


s_dato_l = []
s_tid_l = []
s_trykk_l = []
s_temp_l = []

for linje in fil_solatime:
    if linje.split(";")[0] == "Sola":
        s_date, s_time, s_trykk, s_temp = splitsolatime(linje)
        s_dato_l.append(s_date)
        s_tid_l.append(s_time)
        s_trykk_l.append(s_trykk)
        s_temp_l.append(s_temp)

s_dato_tid_l = []

for i in range (len(s_dato_l)):
    s_dato_tid_l.append(s_dato_l[i] + " " + s_tid_l[i])



print("Her er dato:", "\n", s_dato_l, "\n")
print("Her er tid:", "\n", s_tid_l, "\n")
print("Her er temp:", "\n", s_temp_l, "\n")
print("Her er trykk:", "\n", s_trykk_l, "\n")
print("Her er dato og tid sammen", "\n", s_dato_tid_l, "\n")

plt.plot(s_dato_tid_l, s_temp_l)
plt.plot(s_dato_tid_l, s_trykk_l)
plt.xticks(["11.06.2021 01:00", "12.06.2021 00:00", "13.06.2021 00:00", "14.06.2021 00:00"])
#plt.yticks([10, 100, 500, 1000, 2000])



print(len(s_dato_tid_l))
print(len(s_temp_l))
print(len(s_trykk_l))

plt.show()
#datetime_liste = d.datetime(s_dato_tid_l)
fil_solatime.close()