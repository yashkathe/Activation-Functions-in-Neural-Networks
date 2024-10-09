import matplotlib.pyplot as plt
import numpy as np

# define input points (we'll use a 2D array since softmax works on vectors)
logits = np.random.rand(3)

# softmax function
def summationFn(logits):
    summation = 0
    
    for logit in logits:
        summation += np.exp(logit)
    
    return summation

summation = summationFn(logits)

def softmaxFn(logits):
    probablities = []

    for logit in logits:
        softmax = np.exp(logit) / summation
        probablities.append(softmax)

    return probablities

# apply softmax function on logits
probablities = softmaxFn(logits)

# verify the sum of probablities as 1
print(sum(probablities))

# plot the softmax results for each set of logits
classes = ['class A', 'class B', 'class C']

plt.bar(classes, probablities)
plt.xlabel("Inputs")
plt.ylabel("Softmax output")
plt.title("Graph of Softmax Function")
plt.legend()
plt.show()
