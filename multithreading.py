import time
from threading import Thread


summ = 0.0
cof_1, cof_2 = 13.0, 7.0


def pot(cof):
    global summ
    for i in range(10):
        summ = summm(summ, cof)


def summm(summ, cof):
    time.sleep(0.01)
    return summ + cof


print("START")

t_1 = Thread(target=pot(cof_1), args=(), daemon=True)
t_2 = Thread(target=pot(cof_2), args=(), daemon=True)

t_1.start()
t_2.start()

while t_1.is_alive() or t_2.is_alive():
    t_1.join(timeout=1)
    print("...")

print(summ)
