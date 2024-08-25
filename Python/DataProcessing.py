import Experiment
import numpy as np
import csv

percentages = np.linspace(5,97,93).astype(int)
# print(percentages)

experimentCount = 1000

experiments = []

for i in range(0,experimentCount):
    file = "../Data/Raw/out" + str(i) + ".csv"
    print("Reading file \"" + file + "\"")

    experiment = Experiment.Experiment(file)
    experiments.append(experiment)

time = {}

for percentage in percentages:
    time[percentage] = []

for experiment in experiments:
    times = np.interp(percentages,experiment.percentage,experiment.cumulativeDuration)
    for i in range(len(percentages)):
        time[percentages[i]].append(float(times[i]))

for percentage in percentages:
    file = "../Data/Processed/percentage" + str(percentage) + ".csv"
    print("Writing file \"" + file + "\"")
    with open(file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ExperimentId","Time"])

        for i in range(experimentCount):
            writer.writerow([str(i),str(time[percentage][i])])
