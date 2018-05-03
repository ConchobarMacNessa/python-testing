import numpy as np
w1 = np.array([[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6]])
w2 = np.zeros((1, 3))
w2[0,:] = np.array([0.5, 0.5, 0.5])
b1 = np.array([0.8, 0.8, 0.8])
b2 = np.array([0.2])
def f(x):
    return 1 / (1 + np.exp(-x))
