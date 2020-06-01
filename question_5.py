'''
Box-Muller method
'''

import numpy as np
import matplotlib.pyplot as plt

#Gausssian with mean 0 and variance 1
def gaussian(x):
	return np.exp(-x**2/2)/np.sqrt(2*np.pi)

x1 = np.random.rand(100000)
x2 = np.random.rand(100000)
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

xplt = np.linspace(-5,5,100)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.hist(x1, density = True, color = "C1", rwidth = 0.9)
ax1.set_xlabel('xi')
ax1.set_ylabel('PDF')
ax1.set_xlim(0,1)
ax1.set_title("PDF of uniform distribution")


ax2.hist(x2, density = True, color = "C1", rwidth = 0.9)
ax2.set_xlabel('xi')
ax2.set_ylabel('PDF')
ax2.set_xlim(0,1)
ax2.set_title("PDF of uniform distribution")

ax3.hist(y1, density = True, color = "C1", rwidth = 0.9)
ax3.plot(xplt, gaussian(xplt),'m', label = 'Gaussian PDF')
ax3.set_xlabel('y1')
ax3.set_ylabel('PDF')
ax3.legend()
ax3.set_title("PDF of Gaussian distribution")

ax4.hist(y2, density = True, color = "C1", rwidth = 0.9)
ax4.plot(xplt, gaussian(xplt),'m', label = 'Gaussian PDF')
ax4.set_xlabel('y2')
ax4.set_ylabel('PDF')
ax4.legend()
ax4.set_title("PDF of Gaussian distribution")

plt.show()

