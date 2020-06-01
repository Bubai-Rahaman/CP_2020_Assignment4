"""
Time comparision between Linera congruential generator and Numpy code
"""

import numpy as np
from scipy.stats import uniform
import time

def LGC(x,N):

	a = 1664525
	c = 1013904223
	m = 4294967296
	results = []
	
	for i in range(N):
		x = (a*x+c)%m
		results.append(x)
	return results
	
N = 10000
#Linear congruential generator
start_time1 = time.time()
x1 = LGC(1,N)
x2 = LGC(5,N)
rand = np.zeros(N)
for i in range(N):
	if (x1[i]>x2[i]):
		rand[i] = x2[i]/x1[i]
	elif (x1[i] == 0 and x2[i] == 0):
		rand[i] = 0
	else:
		rand[i] = x1[i]/x2[i]
end_time1 = time.time()

#Numpy.random.rand()
start_time2 = time.time()
random = np.random.rand(N)
end_time2 = time.time()

print("Time take by Linear conguential generator to produce 10000 uniform deviates is",(end_time1-start_time1),"sec and numpy function took",(end_time2-start_time2),"sec")
