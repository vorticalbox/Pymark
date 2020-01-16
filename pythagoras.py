from multiprocessing import Process, cpu_count
from time import time
import math


def timer(func):
	def f(*args, **kwargs):
		before = time()
		rv = func(*args, **kwargs)
		after = time()
		dif = after - before
	##	calcs = n / dif 
	## Note: n is the number of calculations run by the start methods. To-do: Find a way to pass N to here.
		print('elapsed', dif)
	##	print('Calculations per second:', calcs)
		return rv
	return f

def int_calc(x):
	c = math.sqrt((x**2)+(x**2))


def float_calc(x):
	while x > 1:
		x *= 0.9999


def process_target(func, count, offset, step):
	for i in range(offset, count, step):
		func(i)

@timer
def calculate(func, num, cores):
	processes = [Process(target=process_target, args=(func, num, x, cores), daemon=True) for x in range(cores)]
	for p in processes:
		p.start()
	
	for p in processes:
		p.join()
	
	
def start_int(n):
	print("Starting {} integer calculations with 1 thread".format(n))
	calculate(int_calc, n, 1)
	print("Starting {} integer calculations with {} threads".format(n, cpu_count()))
	calculate(int_calc, n, cpu_count())
    

def start_float(n):
	print("Starting {} float calculations with 1 thread".format(n))
	calculate(float_calc, n, 1)
	print("Starting {} float calculations with {} threads".format(n, cpu_count()))
	calculate(float_calc, n, cpu_count())


if __name__ == '__main__':

	start_int(10**7)
	start_float(10**4)
