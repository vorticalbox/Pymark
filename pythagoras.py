from multiprocessing import Pool,cpu_count
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


def create_list(n):
	for i in range(n):
		yield i


@timer
def calculate(func, list, cores):
	with Pool(cores) as p:
		p.map(func,list)


def start_int(n):
	print("Starting {} integer calculations with 1 thread".format(n))
	calculate(int_calc, create_list(n), 1)
	print("Starting {} integer calculations with {} threads".format(n, cpu_count()))
	calculate(int_calc, create_list(n), cpu_count())
    

def start_float(n):
	print("Starting {} float calculations with 1 thread".format(n))
	calculate(float_calc, create_list(n), 1)
	print("Starting {} float calculations with {} threads".format(n, cpu_count()))
	calculate(float_calc, create_list(n), cpu_count())


if __name__ == '__main__':

	start_int(10**7)
	start_float(10**4)
