import matplotlib.pyplot as plt
import numpy as np

# define input points
inputs = np.arange(-5,6)

# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# apply relu function on inputs
results = []

for x in inputs:
    result = sigmoid(x)
    results.append(result)

# plot the results of relu function
plt.plot(inputs, results)
plt.xlabel('Inputs')
plt.ylabel('Sigmoid output')
plt.title('Graph of Sigmoid Function')
plt.grid()
plt.show()