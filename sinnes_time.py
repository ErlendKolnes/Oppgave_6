#from splitfunksjon import splitfunksjon
from sola_time import splitsolatime
import datetime as d
import matplotlib.pyplot as plt

si_dato_l =[]
si_temp_l = []
si_trykk_l = []
si_tid_l = []



with open("sinnes_time.csv.txt", "r", encoding="UTF8") as sinnes_time:
    for linje in sinnes_time:
        if linje.split(";")[0] == "Sirdal - Sinnes":
            si_dato, si_tid, si_trykk, si_temp = splitsolatime(linje)
            si_dato_l.append(si_dato)
            si_tid_l.append(si_tid)
            si_trykk_l.append(si_trykk)
            si_temp_l.append(si_temp)

si_ny_dato = []
si_ny_tid = []
for i in range(len(si_dato_l)):
    si_ny_dato.append(si_dato_l[i].split("."))
    si_ny_tid.append(si_tid_l[i].split(":"))


si_dt_dato = []
for i in range(len(si_ny_dato)):
    dag = d.datetime(int(si_ny_dato[i][2]), int(si_ny_dato[i][1]), int(si_ny_dato[i][0]), int(si_ny_tid[i][0]), int(si_ny_tid[i][1]), int("00"))
    si_dt_dato.append(dag)

if __name__ == "__main__":
    plt.subplot(2, 1, 1)
    plt.plot(si_dt_dato, si_temp_l, label="Temperatur Sinnes", color="green")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(si_dt_dato, si_trykk_l, label="Trykk Sinnes", color="blue")
    plt.legend()
    plt.show()