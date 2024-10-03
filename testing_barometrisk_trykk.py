#testing_tom_index_barometrisk

import datetime as d
import matplotlib.pyplot as plt

barometrisk_trykk = []

#Testliste
for i in range(19):
    if i%6 == 0:
        barometrisk_trykk.append(i*100)
    else:
        barometrisk_trykk.append("")

# print(barometrisk_trykk)

teller = 0
for linje in barometrisk_trykk:
    if linje == "":
        barometrisk_trykk[teller] = barometrisk_trykk[teller-1]
    teller += 1

print(barometrisk_trykk)


# dt_liste_test = []
# for i in range(19):
#     dag = d.datetime(2021, 6, 11+i)
#     dt_liste_test.append(dag)

#print(dt_liste_test)

# plt.plot(dt_liste_test, barometrisk_trykk, label="Test barometrisk trykk", color="orange", marker="X")
# plt.legend()

# plt.show()