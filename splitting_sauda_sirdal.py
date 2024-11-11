
with open("temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt", "r", encoding="UTF8") as samlet_fil:
    for linje in samlet_fil:
        if linje.split(";")[0] == "Sirdal - Sinnes":
            with open("sinnes_time.csv.txt", "a", encoding="UTF8") as sinnes_time:
                sinnes_time.write(linje)
        elif linje.split(";")[0] == "Sauda":
            with open("sauda_time.csv.txt", "a", encoding="UTF8") as sauda_time:
                sauda_time.write(linje)

