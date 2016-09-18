from multiprocessing import Pool
from datetime import datetime
import math
units = 1
myList = [] 
def f(x):
    c = math.sqrt((x**2)+(x**2))

def createList(calc):
    myList = [i+1 for i in range(calc)]

def startBench(threads):
    for i in range(1,threads+1):
        print("Started using {} thread(s)".format(i))
        startTime = datetime.now()
        p = Pool(i)
        p.map(f, myList)
        print("Took {} with {} thread(s)".format((datetime.now() - startTime).total_seconds(), i))

if __name__ == '__main__':
    print("creating list {}".format(datetime.now()))
    createList(10**6)
    print("List created {}".format(datetime.now()))
    print("Starting {} calculations".format(len(myList)))
    startBench(int(input('Enter CPU Threads : ')))
    print("end")
