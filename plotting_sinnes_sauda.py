from sinnes_time import *
from sauda_time import *

if __name__ == "__main__":
    plt.subplot(2, 1, 1)
    plt.plot(si_dt_dato, si_temp_l, label="Temperatur Sinnes", color="green")
    plt.plot(sau_dt_dato, sau_temp_l, label="Temperatur Sauda", color="blue")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(si_dt_dato, si_trykk_l, label="Trykk Sinnes", color="green")
    plt.plot(sau_dt_dato, sau_trykk_l, label="Trykk Sauda", color="blue")
    plt.legend()
    plt.show()