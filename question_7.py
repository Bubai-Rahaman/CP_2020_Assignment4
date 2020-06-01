'''
Chi square test
'''
import numpy as np
from scipy.stats import chi2 

def chi_test(v):
	v = v*100
	if (v < 1.0 or v > 99.0):
		print("not sufficiently random")
	elif(1.0 < v < 5.0 or 95.0 < v < 99.0):
		print("suspect")
	elif( 5.0 < v < 10.0 or 90.0 < v < 95.0):
		print("almost suspect")
	elif( 10.0 < v < 90.0):
		print("sufficiently random")
	return(0)
	
	
expected_counts = np.array((4,8,12,16,20,24,20,16,12,8,4))
observed_counts1 = np.array((4,10,10,13,20,18,18,11,13,14,13))
observed_counts2 = np.array((3,7,11,15,19,24,21,17,13,9,5))

chi_1 = 0
chi_2 = 0
for i in range(expected_counts.size):
	chi_1 = chi_1+((observed_counts1[i]-expected_counts[i])**2)/expected_counts[i]
	chi_2 = chi_2+((observed_counts2[i]-expected_counts[i])**2)/expected_counts[i]

k = 10.0

p1 = 1.0 - chi2.cdf(chi_1, k)
p2 = 1.0 - chi2.cdf(chi_2, k)

#observed counts 1
print("Observed counts 1 numbers are")
chi_test(p1)

#observed counts 2
print("Observed counts 2 numbers are")
chi_test(p2)
