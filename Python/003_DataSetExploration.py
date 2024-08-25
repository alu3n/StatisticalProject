import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

from DataSet import DataSet

# Loading the dataset takes some time...
# If you set experiment count to '-1', it will load the entire dataset
DS = DataSet("../Data/DataSet1", experimentCount=-1)

listInstructionDuration = []
listCumulativeDuration = []
listPercentage = []

# ... Prepare data for processing ...
for E in DS.experiments:
    listInstructionDuration.append(E.duration)
    listCumulativeDuration.append(E.cumulativeDuration)
    listPercentage.append(E.percentage)

instructionDurations = np.vstack(listInstructionDuration)
cumulativeDurations = np.vstack(listCumulativeDuration)
percentages = np.vstack(listPercentage)

# Question: What is the min and max percentage cleaned after certain amount of time?
minimumAfter5000 = np.min(percentages[:,-1])
maximumAfter5000 = np.max(percentages[:,-1])

print("Minimum after 5000 instructions is: " + str(minimumAfter5000) + "%")
print("Maximum after 5000 instructions is: " + str(maximumAfter5000) + "%")


# Question: How does plot of all percentage progressions look like?
fig, ax = plt.subplots()
plt.title("Time to clean %")
plt.xlabel("Target percentage")
plt.ylabel("Time [s]")

# ... Individual cleanups ...
X = np.linspace(0,minimumAfter5000,30)
Y_Values = []
for E in DS.experiments:
    Y_Values.append(np.interp(X,E.percentage,E.cumulativeDuration))

# ... Graph individual runs ...
for Y in Y_Values:
    plt.plot(X,Y,color="orange",alpha=0.5)

# ... Graph bounding curves ...
plt.plot(X,np.min(np.vstack(Y_Values),axis=0),color="g")
plt.plot(X,np.max(np.vstack(Y_Values),axis=0),color="r")

# ... Graph average run curve ...
plt.plot(X,np.mean(np.vstack(Y_Values),axis=0),color="b")

plt.show()

# Question: What is the standard deviation of time it took to clean certain percentage?
fig, ax = plt.subplots()
plt.title("Standard deviation of cleaning time")
plt.xlabel("Target percentage")
plt.ylabel("Time [s]")
plt.plot(X,np.std(np.vstack(Y_Values),axis=0),color="g")

plt.show()

# Question: How does distribution of times to clean specific percentage look like?
targetPercentage = 90

measuredTimes = []
for E in DS.experiments:
    measuredTimes.append(float(np.interp(targetPercentage,E.percentage,E.cumulativeDuration)))

# ... Plot histogram and ecdf...
fig, ax = plt.subplots()
plt.title("Time it took to clean 90%")

plt.hist(measuredTimes,bins=22)

# ... Evaluate ecdf ...
# cdf = scipy.stats.ecdf(measuredTimes)
ecdf_dist = scipy.stats.ecdf(measuredTimes)
X = np.linspace(np.min(measuredTimes)-200,np.max(measuredTimes)+200,500)

fig, ax = plt.subplots()
plt.title("Empirical CDF")

ecdf_dist.cdf.plot(ax)
plt.show()

# Form a hypotheses
shape, loc, scale = scipy.stats.lognorm.fit(measuredTimes)
lognorm_dist = scipy.stats.lognorm(shape,loc=loc,scale=scale)

fig, ax = plt.subplots()
plt.title("Estimation")

ecdf_dist.cdf.plot(ax)
ax.plot(X,lognorm_dist.cdf(X),color="green")
plt.show()

print("Shape = " + str(shape))
print("Loc = " + str(loc))
print("Scale = " + str(scale))

