def splitfunksjon(data):

    # Del strengen ved semikolon
    s_parts = data.split(';')
    
    # Hent dato og tid
    s_date_time = s_parts[2].split()
    if len(s_date_time) != 0: #For å unngå feil ved "siste linje"
        s_date = s_date_time[0]
        s_time = s_date_time[1]
    
    

    # Hent trykk
    s_trykk_n = s_parts[4].replace(",", ".")
    s_trykk = float(s_trykk_n) / 10 #Fjerner newline-tegn, gjør om til float-variabel

    # Hent tempertur
    s_temp_n = s_parts[3].replace(",", ".")
    s_temp = float(s_temp_n) #Gjør om til float-variabel
    
    return s_date, s_time, s_trykk, s_temp