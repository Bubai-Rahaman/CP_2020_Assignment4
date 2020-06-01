'''
Random number between 0 and 1 using Numpy
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import time

N = 10000
start_time = time.time()
random = np.random.rand(N)
end_time = time.time()

x = np.linspace(0,1,10000)
PDF = uniform.pdf(x)
print("Time required to produce",N,"uniform deviates is",(end_time-start_time),'sec')

plt.hist(random, range=(0.0,1.0), density = True, rwidth = 0.9, color = "C1")
plt.plot(x,PDF,'b',label = 'Uniform PDF ')
plt.xlabel("x")
plt.ylabel('PDF')
plt.xlim(0,1)
plt.title("A PDF of 10000 uniform deviates between 0 and 1")
plt.legend()

plt.show()

