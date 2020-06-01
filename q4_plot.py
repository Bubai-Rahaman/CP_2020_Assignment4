import numpy as np
import matplotlib.pyplot as plt

def exp(x):
	return 2*np.exp(-2*x)

#importing data
x = np.loadtxt("q_4_data.txt", usecols = 0)
y = np.loadtxt("q_4_data.txt", usecols = 1)

xplot = np.linspace(0,15,100)

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.hist(x ,color = "C1", density = True, rwidth = 0.9)
ax1.set_xlabel("x")
ax1.set_ylabel("PDF")
ax1.set_xlim(0,1)
ax1.set_title("PDF of unifrom distrubution")

ax2.hist(y, color = "C1", density = True, rwidth = 0.9)
ax2.plot(xplot, exp(xplot),'g', label = "2exp(-2x)")
ax2.set_xlabel("y")
ax2.set_ylabel("PDF")
ax2.set_xlim(0,10)
ax2.legend()
ax2.set_title("PDF of exponential distrubution")

plt.show()
