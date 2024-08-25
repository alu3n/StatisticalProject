import csv
import numpy as np

class Experiment:
    def __init__(self, fileName):
        with open(fileName, "r") as f:
            reader = csv.reader(f)
            data = np.array(list(reader)[1:-1])
        self.duration = data[:, 1].astype(float)
        self.collected = data[:, 2].astype(int)
        self.cumulativeCollected = data[:, 3].astype(int)
        self.percentage = data[:, 4].astype(float)
        self.cumulativeDuration = data[:, 5].astype(float)