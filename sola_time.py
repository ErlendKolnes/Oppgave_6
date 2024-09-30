# Funksjon for å dele opp strengen i komponenter






def splitsolatime(data):
    #parts = data.replace(';;', ';')


    # Del strengen ved semikolon
    s_parts = data.split(';')
    
    #if len(parts) < 5 or not parts[0] or not parts[1] or not parts[2] or not parts[3] or not parts[4]:
        
        #return None

    # Hent dato og tid fra første del
    s_date_time = s_parts[2].split()
    if len(s_date_time) != 0:
        s_date = s_date_time[0]
        s_time = s_date_time[1]
        
    # Hent andre målinger
    s_trykk = s_parts[4].replace(",", ".")
    s_temp = s_parts[3].replace(",", ".")
    
    return s_date, s_time, s_trykk, s_temp

fil_solatime_streng = ""

fil_solatime = open("sola_time.csv.txt", "r", encoding="UTF8")
# for linje in fil_solatime:
#     fil_solatime_streng +=linje

#print(fil_solatime_streng)
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

print("Her er dato:", "\n", s_dato_l, "\n")
print("Her er tid:", "\n", s_tid_l, "\n")
print("Her er temp:", "\n", s_temp_l, "\n")
print("Her er trykk:", "\n", s_trykk_l, "\n")

fil_solatime.close()