import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import goodness_of_fit

from DataSet import DataSet

DS = DataSet("../Data/DataSet2/", experimentCount=-1)

targetPercentage = 90

measuredTimes = []
for E in DS.experiments:
    measuredTimes.append(float(np.interp(targetPercentage,E.percentage,E.cumulativeDuration)))

s = 0.4489822310415079
loc = 1982.106368481833
scale = 651.5013077189651


lognorm_dist = scipy.stats.lognorm(s=s,loc=loc,scale=scale)

ksTest = scipy.stats.kstest(measuredTimes,lognorm_dist.cdf)

print(ksTest)

# ... Evaluate ecdf ...
# cdf = scipy.stats.ecdf(measuredTimes)
ecdf_dist = scipy.stats.ecdf(measuredTimes)
X = np.linspace(np.min(measuredTimes)-200,np.max(measuredTimes)+200,500)

fig, ax = plt.subplots()
plt.title("ECDF (DS2) vs. hypothesis CDF")

ecdf_dist.cdf.plot(ax,color="red")
ax.plot(X,lognorm_dist.cdf(X),color="green")
plt.show()