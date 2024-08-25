import numpy as np
import matplotlib.pyplot as plt
from Experiment import Experiment

E = Experiment("../Data/DataSet1/Experiment1.csv")

### SEKCE 3.1 - O jednotlivych instrukcich ###
shortestInstruction = np.min(E.duration)
longestInstruction = np.max(E.duration)
averageInstruction = np.mean(E.duration)

print("Shortest instruction duration: "+ str(shortestInstruction))
print("Longest instruction duration: "+str(longestInstruction))
print("Average instruction duration: "+str(averageInstruction))

# Because even instructions are move, and odd instructions are rotate
moveInstructionsTimes = E.duration[0::2]
rotateInstructionsTimes = E.duration[1::2]

averageMoveTime = np.average(moveInstructionsTimes)
averageRotateTime = np.average(rotateInstructionsTimes)

print("Average move instruction duration: " + str(averageMoveTime))
print("Average rotate instruction duration: " + str(averageRotateTime))

### SEKCE 3.2 - Rozdeleni trvani instrukci ###
fig, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.hist(moveInstructionsTimes,bins=50)
ax1.set_title('Move Instructions Times')
ax2.hist(rotateInstructionsTimes,bins=50)
ax2.set_title('Rotate Instructions Times')
ax3.hist(E.duration,bins=50)
ax3.set_title('Combined Instruction Times')
plt.show()

### SEKCE 3.3 - O celkovem prubehu ###
fig, ax = plt.subplots()
ax.plot(E.percentage,E.cumulativeDuration)
plt.xlabel("Percentage")
plt.ylabel("Duration [s]")
plt.show()

totalDuration = np.max(E.cumulativeDuration)
totalPercentage = np.max(E.percentage)

print("Total duration: " + str(totalDuration))
print("Total percentage: " + str(totalPercentage))




# sampleMeanInstructionDuration = np.mean(E.duration)
# maxPercentage = np.max(E.percentage)
# totalDuration = np.max(E.cumulativeDuration)
#
# # Print basic information
# print("Expected instruction duration: " + str(round(sampleMeanInstructionDuration,2)) + "s")
# print("Cleaned after 5000 instructions: " + str(round(maxPercentage,2)) + "%")
# print("Total duration: " + str(round(totalDuration,2)) + "s")
#
#
# # Plot the graph X - Percentage; Y - Time
# fig, ax = plt.subplots()
# plt.title("Experiment 0")
# plt.xlabel("Percentage")
# plt.ylabel("Time [s]")
#
# plt.axvline(x=maxPercentage, color='r', linestyle='--')
# ax.plot(E.percentage,E.cumulativeDuration,color='g')
# ax.text(maxPercentage+1,totalDuration/2,str(round(maxPercentage,2)) + "%",
#         ha="left", va="top",color='r')
# plt.show()