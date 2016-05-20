import random
import sys

def contruct_data(f):
    fp = open(f[0], 'w')
    for i in range(40):
        name = "%s name_%s %s :%s\n"%(i, i, f[1], random.randint(50, 100))
        fp.writelines(name)
    fp.close()

if __name__ == '__main__':
    argv = sys.argv[1:]
    print argv
    contruct_data(argv)