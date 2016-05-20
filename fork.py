from multiprocessing import Process
import os
import time
os.write
p = os.pipe()

def run_proc(name):
    os.close(p[1])
    msg = os.read(p[0], 1024)
    print(msg)
    for i in range(3):
        time.sleep(1)
        print("Run Child Process %s (%s)..."%(name, os.getpid()))

if __name__ == "__main__":
    print("Parent process %s" % os.getpid())
    os.close(p[0])
    os.write(p[1], bytes("Hello Pipe", encoding = 'utf-8'))
    p = Process(target = run_proc, args = ('test',))
    print("Process wil start")
    p.start()
    p.join()
    print("Process End!")