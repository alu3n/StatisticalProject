from Experiment import Experiment
import os
from pathlib import Path

class DataSet:
    def __init__(self, rawDataFolderPath, experimentCount = -1):
        directory = Path(rawDataFolderPath)
        files = [str(f) for f in directory.iterdir() if f.is_file()]
        self.experiments = []

        count = 1

        maxCount = len(files) if experimentCount == -1 else min(experimentCount, len(files))

        for file in files:
            print("Loading file: " + str(count) + " of " + str(maxCount))
            self.experiments.append(Experiment(file))
            count += 1
            #TODO: Remove this cond
            if count > maxCount:
                break
