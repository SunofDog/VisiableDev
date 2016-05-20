import os
import time
from multiprocessing import Queue, Process, Value, Array

g_va = Value('i', 0)
g_ar = Array('i', range(1000))
def child_func(g_value, g_array, ar):
    g_value.value = ar
    g_array[ar] = ar*ar

if __name__ == "__main__":
    start = time.time()
    listp = []
    for i in range(1000):
        p = Process(target = child_func, args = (g_va, g_ar, i))
        p.start()
        listp.append(p)
    for i in range(1000):
        listp[i].join()
    print(g_va.value)
    print(g_ar[:])
    print("%s s"%time.time() - start)
