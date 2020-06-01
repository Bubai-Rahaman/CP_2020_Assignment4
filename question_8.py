'''
Circle area and volume of 1d unit sphere using monte carlo integration
'''

import numpy as np

#function for circle
def f(x,y):
	#return x**2 + y**2
	if(x**2 + y**2<=1):
		return 1
	else:
		return 0
	
N = 100000

x = np.random.rand(N)
y = np.random.rand(N)

k = 0
'''
for i in range(N):
	if (f(x[i],y[i]) <= 1):
		k = k + 1
	else:
		continue
print(4*k*1/N)
'''
s = 0 
for i in range(N):
	s += f(x[i],y[i])
s = s/N

print("Area of the circle is",4*s)

#function for 10d sphere
def f_10d(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
	if(x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2 + x7**2 + x8**2 + x9**2 + x10**2 <= 1):
		return 1
	else:
		return 0
x1 = np.random.rand(N,10)

s = 0 
for i in range(N):
	s += f_10d(x1[i,0],x1[i,1],x1[i,2],x1[i,3],x1[i,4],x1[i,5],x1[i,6],x1[i,7],x1[i,8],x1[i,9])
s = s/N
print("Volume of the 10d sphere is",(2**10)*s)
