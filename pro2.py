import os
import time
from multiprocessing import Queue, Process, Value, Arrary

g_va = Value('i', 0)
g_ar = Arrary('i', range(10))
def child_func(g_value, g_array, ar):
    g_value.value = ar
    g_array[ar] = ar*ar

if __name__ == "__main__":
    listp = []
    for i in range(10):
        p = Process(target = child_func, args = (g_va, g_ar, i))
        p.start()
        listp.append(p)
    for i in range(10)
        listp[i].join()
    print g_va.Value
    print g_ar[:]
