from multiprocessing import Pool,cpu_count
from datetime import datetime
import math

calc =[]
def i(x):
    c = math.sqrt((x**2)+(x**2))
def f(x):
    while x > 1:
        x *= 0.9999
def createList(n):
    for i in range(n):
        calc.append(i)
def startInt():
    threads = cpu_count()
    print("Creating list.")
    createList(10**7)
    print("List created")
    print("Starting {} intger calculations with 1 thread".format(len(calc)))
    startTime = datetime.now()
    p = Pool(1)
    p.map(i, calc)
    print("Took {} with 1 thread(s)".format((datetime.now() - startTime).total_seconds()))
    #multi core test#
    if threads > 1:
        print("Starting {} calculations with {} threads".format(len(calc), threads))
        startTime = datetime.now()
        p = Pool(threads)
        p.map(i, calc)
        print("Took {} with {} thread(s)".format((datetime.now() - startTime).total_seconds(), threads))
    else:
        print('Single core CPU skipping test')
    calc[:] = []
def startFloat():
    threads = cpu_count()
    print('Warning! float calculations can take a long time')
    #multi core test#
    if threads >= 4:
        print("Creating list.")
        createList(10**4)
        print("List created")
        print("Starting {} calculations with {} threads".format(len(calc), threads))
        startTime = datetime.now()
        p = Pool(threads)
        p.map(f, calc)
        print("Took {} with {} thread(s)".format((datetime.now() - startTime).total_seconds(), threads))
    else:
        print('Float test takes too long with < 4 threads')
    calc[:] = []
if __name__ == '__main__':
    #startInt()
    startFloat()
