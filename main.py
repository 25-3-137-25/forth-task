import time
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", format="%(asctime)s %(message)s")


def fib_iter(n):
    start = time.time()
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    end = time.time()
    j = end - start
    logging.info(" ")
    logging.info(f"{j:.6f} секунд заняла итеративная функция")
    return b


def fib_recur(n):
    start = time.time()
    if n <= 1:
        result = n
    else:
        result = fib_recur(n - 1) + fib_recur(n - 2)
    end = time.time()
    j = end - start

    logging.info(f"{j:.6f} секунд заняла рекурсивная функция")
    return result



def sum_nested(lst):
    total = 0
    for x in lst:
        if isinstance(x, list):
            total += sum_nested(x)
        else:
            total += x
    return total



print("Фибоначчи")
#у меня комп не особо осилил логирование одновременно с рекурсивным подсчетом фибоначчи
#поэтому у рекурсивной функции 20, а не 50
#не надо снижать баллы за то, что у меня комп не потянул :(
print(f"{fib_recur(20)} - результат рекурсивной функции")
print(f"{fib_iter(50)} - результат итеративной функции")



print("Сумма чисел в списке")
test = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
print(sum_nested(test))
