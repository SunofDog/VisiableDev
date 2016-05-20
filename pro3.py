import os
import time
from multiprocessing import Queue, Process, Value, Array, Manager

g_va = Value('i', 0)
g_ar = Array('i', range(1000))
ma = Manager()
g_dict = ma.dict()
def child_func(g_value, g_array,g_d, ar):
    tmp = ar*ar
    g_value.value = ar
    g_array[ar] = tmp
    g_d[ar] = tmp

if __name__ == "__main__":
    start = time.time()
    listp = []
    for i in range(1000):
        p = Process(target = child_func, args = (g_va, g_ar, g_dict, i))
        p.start()
        listp.append(p)
    for i in range(1000):
        listp[i].join()
    print g_va.value
    print g_ar[:]
    print g_dict
    print time.time() - start
