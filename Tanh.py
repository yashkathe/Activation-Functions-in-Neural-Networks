import matplotlib.pyplot as plt
import numpy as np

# define input points
inputs = np.arange(-5, 6)

# tanh function
def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# apply tanh function on inputs
results = []

for x in inputs:
    result = tanh(x)
    results.append(result)

# plot the results of tanh function
plt.plot(inputs, results)
plt.xlabel("Inputs")
plt.ylabel("Tanh output")
plt.title("Graph of Tanh Function")
plt.grid()
plt.show()
