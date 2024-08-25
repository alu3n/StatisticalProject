import numpy
import numpy as np
import matplotlib.pyplot as plt

import Experiment
import csv
from scipy.stats import lognorm
import scipy

percentage = 90

times = []

file = "../Data/Processed/percentage" + str(percentage) + ".csv"

with open(file, "r") as f:
    reader = csv.reader(f)
    data = np.array(list(reader)[1:-1])
    times = data[:,1].astype(float)


minTime = np.min(times)
maxTime = np.max(times)

sampleMean = np.mean(times)
sampleVar = np.var(times,ddof=1)
sampleStd = np.std(times)



# Given mean and standard deviation of the log-normal distribution
mean_log = sampleMean  # replace with your value
stdev_log = sampleStd  # replace with your value

# Convert to mu and sigma of the underlying normal distribution
mu = np.log(mean_log**2 / np.sqrt(stdev_log**2 + mean_log**2))
sigma = np.sqrt(np.log(stdev_log**2 / mean_log**2 + 1))

shape, loc, scale = lognorm.fit(times[:500])

lognorm_dist = lognorm(shape,loc=loc,scale=scale)
ecdf_dist = scipy.stats.ecdf(times[500:])

X = np.linspace(minTime,maxTime,200)
Y = lognorm_dist.cdf(X)

ax = plt.subplot()
ecdf_dist.cdf.plot(ax)
ax.plot(X,Y)
plt.show()

# x = np.linspace(lognorm_dist.cdf(0.01), lognorm_dist.cdf(0.99), 100)
# plt.plot(x, lognorm_dist.cdf(x), 'r-', lw=2, label='lognorm pdf')
# plt.title('Log-Normal Distribution')
# plt.xlabel('x')
# plt.ylabel('Probability Density')
# plt.legend()
# plt.show()






print("Minimum time: " + str(minTime))
print("Maximum time: " + str(maxTime))
print("Sample mean: " + str(sampleMean))
print("Sample variance: " + str(sampleVar))
print("Sample standard deviation: " + str(sampleStd))

X, Y = numpy.histogram(times,bins=20)
# print(plot)

fig, ax = plt.subplots()
ax.hist(times,bins=22)
plt.show()