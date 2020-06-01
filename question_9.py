import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def f(x):
	if 3<x<7:
		return 1
	else:
		return 0

N = 10000
theta = 5.0
x = []
xp = []

for i in range(N):
	theta_prime = theta + np.random.standard_normal()
	r = np.random.rand()
	
	xp.append(theta_prime)
	if f(theta) == 0:
		theta = theta_prime
	elif f(theta_prime)/f(theta) > r:
		theta = theta_prime
	x.append(theta)

step = np.arange(1,N+1,1)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)


xplot = np.linspace(2,8,200)
fplot = np.zeros(200)
for i in range(200):
	fplot[i] = 0.25*f(xplot[i])

#Histogram
plt.figure()
plt.hist(x, range = (3.0, 7.0), density = True, rwidth = 0.9, bins = 10)
plt.plot(xplot, fplot, 'm', label = 'PDF')
plt.legend()
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Histogram')
plt.xlim(2,8)

#ax2.plot(step, xp, 'm.', label = 'Rejected points')
ax1.plot(step, x, 'b.-', label = 'Markov chain')
ax1.legend()
ax1.set_xlabel('step')
ax1.set_ylabel('theta')
ax1.set_title('Markov chain of 10000 points')


#ax3.plot(step, xp, 'm.', label = 'Rejected points')
ax2.plot(step, x, 'b.-', label = 'Markov chain')
ax2.legend()
ax2.set_xlabel('step')
ax2.set_ylabel('theta')
ax2.set_xlim(0,50)
ax2.set_title('Markov chain of 50 points')

plt.show()
