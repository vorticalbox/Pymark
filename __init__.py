from multiprocessing import Pool
from datetime import datetime
import math

myList = []

def f(x):
    c = math.sqrt((x**2)+(x**2))

def createList(calc):
    for i in range(calc):
        myList.append(i*1)
        
def startBench(threads):
    for i in range(1,threads+1):
        print("Started using {} thread(s)".format(i))
        startTime = datetime.now()
        p = Pool(i)
        p.map(f, myList)
        print("Took {} with {} thread(s)".format((datetime.now() - startTime).total_seconds(), i))

if __name__ == '__main__':
    print("creating list {}".format(datetime.now()))
    createList(10**7)
    print("List created {}".format(datetime.now()))
    print("Starting {} calculations".format(len(myList)))
    startBench(int(input('Enter CPU Threads : ')))
    print("end")
