# A simple neural network - with one input layer, and one output layer
# - capable of finding a linear decision boundary
# - not capable of finding non-linear boundaries

import numpy as np
from matplotlib import pyplot as plt


input = np.linspace(-10, 10, 100)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

# from matplotlib import pyplot as plt
# plt.plot(input, sigmoid(input), c="r")
# plt.show()

# Create feature, and labels set
feature_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])
labels = np.array([[1,0,0,1,1]])
labels_reshape = labels.reshape(5,1)

# Hyper parameters
np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05

# number of times to train the algo on data
for epoch in range(20000):
    inputs = feature_set

    # feedforward step 1
    XW = np.dot(feature_set, weights) + bias

    # feedforward step 2
    z = sigmoid(XW)

    # backpropagation step 1
    error = z - labels_reshape

    print(error.sum())

    # backpropagastion step 2
    dcost_dpred = error
    dpred_dz = sigmoid_der(z)

    z_delta = dcost_dpred * dpred_dz

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num

single_point = np.array([1,0,0]) # yes, no, no
result = sigmoid(np.dot(single_point, weights) + bias)
print(result)

single_point2 = np.array([0,1,0]) # no, yes, no
result2 = sigmoid(np.dot(single_point2, weights) + bias)
print(result2)





# Different methods to display plots:
"""
1. Interative:
from matplotlib import interactive
interactive(True)

2. At the end:
plt.show()

3. Save as PNG:
plt.savefig("temp.png")

"""