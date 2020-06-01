'''
Linear congruential generator
'''
import matplotlib.pyplot as plt
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
start_time = time.time()
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
end_time = time.time()
print("Time required to produce",N,"uniform deviates is",(end_time-start_time),'sec')
x = np.linspace(0,1,10000)
PDF = uniform.pdf(x)

plt.hist(rand, range=(0.0,1.0), density = True, rwidth = 0.9, color = "C1")
plt.plot(x,PDF,'b',label = 'Uniform PDF ')
plt.xlabel("x")
plt.xlim(0,1)
plt.ylabel('PDF')
plt.title("A PDF of 10000 uniform deviates between 0 and 1")
plt.legend()

plt.show()

