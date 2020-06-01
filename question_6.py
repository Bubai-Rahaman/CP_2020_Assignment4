'''
Rejection method
'''

import numpy as np
import matplotlib.pyplot as plt

#Distrubution function
def f(x):
	return np.exp(-x**2/2)*np.sqrt(2/np.pi)

N = 10000
x = np.random.rand(N)*10
y = np.random.rand(N)*0.8

#selecting data
y_bad = y[y > f(x)]
x_bad = x[y > f(x)]

y_good = y[y <= f(x)]
x_good = x[y <= f(x)]

xplot = np.linspace(0,10,100)

#plt.plot(x_bad,y_bad,'r.')
#plt.plot(x_good,y_good, 'b.')

plt.plot(xplot, f(xplot), 'g', label = "Distribution function")
plt.hist(x_good,range = (0.0,10.0), density = True, color = "C1", rwidth = 0.9)
plt.xlim(0,10)
plt.ylim(0,1)
plt.grid()
plt.xlabel('x')
plt.xlabel('f(x)')
plt.legend()
plt.show()
