from math import *
from functools import reduce

import numpy as np


def multivariate_gaussian(x, miu, sigma):
    return 1 / (2 * pi * sigma[0][0] * sigma[1][1]) \
            * exp(-(((x[0] - miu[0]) ** 2 / (2 * sigma[0][0] ** 2) ) + ((x[1] - miu[1]) ** 2 / (2 * sigma[1][1] ** 2))))


sigma = np.array([[0.3, 0],
                  [0, 0.3]])
global_observations = [np.array([6, 3]), np.array([2, 2]), np.array([0, 5])]
associated_landmarks = [np.array([5, 3]), np.array([2, 1]), np.array([4, 7])]

probs = []

for obsv, landmark in zip(global_observations, associated_landmarks):
    probs.append(multivariate_gaussian(obsv, landmark, sigma))

for i, prob in enumerate(probs):
    print('probability of obsv # {}: {}'.format(i, prob))

print('total probability: {}'.format(reduce(lambda x, y: x * y, probs)))

