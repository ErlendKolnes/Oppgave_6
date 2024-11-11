from splitfunksjon import splitfunksjon
import datetime as d
import matplotlib.pyplot as plt

sau_dato_l =[]
sau_temp_l = []
sau_trykk_l = []
sau_tid_l = []



with open("sauda_time.csv.txt", "r", encoding="UTF8") as sinnes_time:
    for linje in sinnes_time:
        if linje.split(";")[0] == "Sauda":
            sau_dato, sau_tid, sau_trykk, sau_temp = splitfunksjon(linje)
            sau_dato_l.append(sau_dato)
            sau_tid_l.append(sau_tid)
            sau_trykk_l.append(sau_trykk)
            sau_temp_l.append(sau_temp)

sau_ny_dato = []
sau_ny_tid = []
for i in range(len(sau_dato_l)):
    sau_ny_dato.append(sau_dato_l[i].split("."))
    sau_ny_tid.append(sau_tid_l[i].split(":"))


sau_dt_dato = []
for i in range(len(sau_ny_dato)):
    dag = d.datetime(int(sau_ny_dato[i][2]), int(sau_ny_dato[i][1]), int(sau_ny_dato[i][0]), int(sau_ny_tid[i][0]), int(sau_ny_tid[i][1]), int("00"))
    sau_dt_dato.append(dag)


if __name__ == "__main__":
    plt.subplot(2, 1, 1)
    plt.plot(sau_dt_dato, sau_temp_l, label="Temperatur Sauda", color="green")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(sau_dt_dato, sau_trykk_l, label="Trykk Sauda", color="blue")
    plt.legend()
    plt.show()