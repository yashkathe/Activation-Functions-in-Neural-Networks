import matplotlib.pyplot as plt
import numpy as np

# define input points
inputs = np.arange(-5,6)

# relu function
def relu(x):
    return max(x, 0)

# apply relu function on inputs
results = []

for x in inputs:
    result = relu(x)
    results.append(result)

# plot the results of relu function
plt.plot(inputs, results)
plt.ylabel('ReLU output')
plt.title('Graph of ReLU Function')
plt.grid()
plt.show()