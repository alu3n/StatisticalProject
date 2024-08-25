import numpy as np
import matplotlib.pyplot as plt
import scipy
import Experiment
import csv

percentages = np.linspace(5,97,93).astype(int)

times = []

for p in percentages:
    file = "../Data/Processed/percentage" + str(p) + ".csv"
    print("Reading file \"" + file + "\"")

    with open(file, "r") as f:
        reader = csv.reader(f)
        data = np.array(list(reader)[1:-1])
        times.append(data[:,1].astype(float))

matrix = np.vstack(times)

fig, ax = plt.subplots()

for i in range(999):
    ax.plot(percentages,matrix[:,i],alpha=0.2)

ax.plot(percentages,np.mean(matrix,axis=1),color="r")

plt.show()