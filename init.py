import threading
import time
tmp = 1
class thread_func(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name = name)

    def run(self):
        for i in range(10):
            # print(threading.activeCount())
            # print(threading.enumerate())
            # print(threading.currentThread())
            time.sleep(1)
            print("Sub Thread %s"%i)

if __name__ == '__main__':
    p1 = thread_func("test1")
    # print(threading.activeCount())
    # print(threading.enumerate())
    # print(threading.currentThread())
    p1.setDaemon(True)
    p1.start()
    time.sleep(11)