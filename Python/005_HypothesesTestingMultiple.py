import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import goodness_of_fit

from DataSet import DataSet

DS1 = DataSet("../Data/DataSet1/", experimentCount=-1)
DS2 = DataSet("../Data/DataSet2/", experimentCount=-1)

targetPercentages = []

targetPercentages = [10,20,30,40,50,60,70,80,90]

for targetPercentage in targetPercentages:
    measuredTimesDS1 = []
    measuredTimesDS2 = []

    for E in DS1.experiments:
        measuredTimesDS1.append(float(np.interp(targetPercentage,E.percentage,E.cumulativeDuration)))
    for E in DS2.experiments:
        measuredTimesDS2.append(float(np.interp(targetPercentage, E.percentage, E.cumulativeDuration)))

    shape, loc, scale = scipy.stats.lognorm.fit(measuredTimesDS1)
    lognorm_dist = scipy.stats.lognorm(s=shape, loc=loc, scale=scale)
    ksTest = scipy.stats.kstest(measuredTimesDS2, lognorm_dist.cdf)
    print(str(targetPercentage) + "%: shape=" + str(shape) + " loc=" + str(loc) + " scale=" + str(scale))
    print("p-value: " + str(ksTest.pvalue))
    print()

s = 0.4489822310415079
loc = 1982.106368481833
scale = 651.5013077189651






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