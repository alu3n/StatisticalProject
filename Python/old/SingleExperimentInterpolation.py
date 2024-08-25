import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy
import Experiment
import csv

experiment = Experiment.Experiment("../Data/Raw/Experiment0.csv")

fig, ax = plt.subplots()
plt.title("Experiment 0")
plt.xlabel("Percentage")
plt.ylabel("Time [s]")

X = np.linspace(5,97,93)
Y = np.interp(X,experiment.percentage,experiment.cumulativeDuration)

ax.plot(X,Y)

plt.show()