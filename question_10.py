'''
Fitting of a model using MCMC
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner

#defining log(L)
def log_likelihood(theta, x, y, yerr):
	a, b, c = theta
	model = a*x**2 + b*x + c
	sigma2 = yerr**2
	
	return 0.5*np.sum((y-model)**2/sigma2 + np.log(2*np.pi*sigma2))

#prior distributation
def log_prior(theta):
	a, b, c = theta
	if -500.0< a < 500 and -500.0< b < 500.0 and -1000.0 < c < 1000.0:
		return 0.0
	return -np.inf

#posterior pdf
def log_probablity(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp - log_likelihood(theta, x, y, yerr)
	
#importing data
x = np.loadtxt("data.txt", delimiter = '&' ,skiprows = 5, usecols = 1)
y = np.loadtxt("data.txt", delimiter = '&' ,skiprows = 5, usecols = 2)
yerr = np.loadtxt("data.txt", delimiter = '&' ,skiprows = 5, usecols = 3)

#initialise markov chain
guess = (1.0, 1.0, 1.0)
soln = minimize(log_likelihood, guess, args = (x, y, yerr))

nwalkers, ndim = 50, 3
pos = soln.x + 1e-4*np.random.randn(nwalkers, ndim)

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probablity, args = (x, y, yerr))
sampler.run_mcmc(pos, 4000)
samples = sampler.get_chain()


#flat samples
flat_samples = sampler.get_chain(flat = True)
medians = np.median(flat_samples, axis = 0)

a_true, b_true, c_true = medians
label = ["a", "b", "c"]
fig = corner.corner(flat_samples, labels = label, truths = [a_true, b_true, c_true])


#Randomly chosen parameter from the posterior
inds = np.random.randint(len(flat_samples), size = 200)
x0 = np.linspace(0,300,500)

plt.figure()
for ind in inds:
	sample = flat_samples[ind]
	plt.plot(x0, np.dot(np.vander(x0,3),sample[:3]),"C1", alpha = 0.1)

plt.errorbar(x, y, yerr = yerr, fmt = ".k", capsize = 0, label = 'Data')
plt.plot(x0, a_true*x0**2 + b_true*x0 + c_true, "k", label = "Best fit model")
plt.legend(fontsize = 14)
plt.xlim(0,300)
plt.xlabel("x")
plt.ylabel("y")

#true value
true_value = (a_true, b_true, c_true)

#error
for i in range(ndim):
	mcmc = np.percentile(flat_samples[:, i], [16,50, 84])
	q = np.diff(mcmc)
	print(label[i],"=",true_value[i],"with one sigma uncertainty (",q[0],",",-q[1],")")

#ploting of markov chain
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

#a
ax1.plot(samples[:, :, 0], 'k', alpha = 0.3)
ax1.set_xlim(0,len(samples))
ax1.set_ylabel('a')
ax1.set_title("Markov chain")

#b
ax2.plot(samples[:, :, 1], 'k', alpha = 0.3)
ax2.set_xlim(0,len(samples))
ax2.set_ylabel('b')

#c
ax3.plot(samples[:, :, 2], 'k', alpha = 0.3)
ax3.set_ylabel('c')
ax3.set_xlim(0,len(samples))
ax3.set_xlabel("Step number")


plt.show()
