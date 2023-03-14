import time
import threading

summ = 0.0         # Переменная доступная всем потокам
cof_1 = 13.0
cof_2 = 7.0
cof_3 = 10.0
lock = threading.Lock()


def pot(cof):       # Функция для оформления потока
    global summ     # Объявление глобальной переменной (доступной из тела функции
    print(threading.current_thread().name + " - начало работы потока с параметром " + str(cof))
    for i in range(10):
                                    # Переменная summ изменяется потоком
        lock.acquire()              # Блокировка
        summ = summm(summ, cof)     # Увеличение значение глобальной переенной.
        lock.release()              # Cнятие блокировки
    print("\n" + threading.current_thread().name + " - конец работы, summ = " + str(summ))


def summm(summ, cof):               # Функция для вычисления суммы
    time.sleep(0.1)                 # Задержка для выявления эффекта рассинхронизации доступа потоков к одной общей переменной
    return summ + cof


print("Поток1 - cоздание потока")
t_1 = threading.Thread(name="Поток1", target=pot, args=([cof_1]), daemon=True)  # Daemon=True - по останову процесса потоки уничтожаются, иначе ожидание останова потоков
print("Поток2 - cоздание потока")
t_2 = threading.Thread(name="Поток2", target=pot, args=([cof_2]), daemon=True)
print("Поток3 - cоздание потока")
t_3 = threading.Thread(name="Поток3", target=pot, args=([cof_3]), daemon=True)

t_1.start()     # Запуск потока на выполнение
t_2.start()     # Запуск потока на выполнение
t_3.start()     # Запуск потока на выполнение


# Ожидание останова потоков
print()
while t_1.is_alive() or t_2.is_alive() or t_3.is_alive():   # Проверка is_alive - жив ли поток?
    print("ждём останова потоков. Активных потоков = " + str(threading.active_count()))
    if t_3.is_alive():
        t_3.join(timeout=0.5)   # Попытка присоединиться к потоку в течении timeout - неудачное название метода
    elif t_2.is_alive():
        t_2.join(timeout=0.5)   # !Это подключение к потоку для ожидание его остановки в течении timeout!
    elif t_1.is_alive():
        t_1.join(timeout=0.5)   # Ожидание остановки потока

# Конец программы
print()
print("Итоговое значение summ = " + str(summ))
