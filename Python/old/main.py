import numpy as np

test1 = np.array([1,2,3])
test2 = np.array([4,5,6])

test = np.vstack((test1,test2))

print(test)
print(test.shape)