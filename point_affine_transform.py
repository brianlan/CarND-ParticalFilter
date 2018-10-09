from math import *

import numpy as np


def rotate(p, theta):
    r = np.array([[cos(theta), sin(theta)], [-sin(theta), cos(theta)]])
    return p.dot(r)


def translate(p, trans):
    return p + trans


def affine_transform_func(p, theta, trans):
    return translate(rotate(p, theta), trans)


def affine_transform_mat(p, theta, trans):
    affine_mat = np.array([[cos(theta), sin(theta), 0],
                           [-sin(theta), cos(theta), 0],
                           [trans[0], trans[1], 1]])
    _p = np.array(p.tolist() + [1])
    return _p.dot(affine_mat)[:2]


car_pos = np.array([4, 5])
car_heading = -pi / 2
obsv1 = np.array([2, 2])
obsv2 = np.array([3, -2])
obsv3 = np.array([0, -4])

print('# rotation + translation')
print(affine_transform_func(obsv1, car_heading, car_pos))
print(affine_transform_func(obsv2, car_heading, car_pos))
print(affine_transform_func(obsv3, car_heading, car_pos))

print('\n# affine transformation in 1 take')
print(affine_transform_mat(obsv1, car_heading, car_pos))
print(affine_transform_mat(obsv2, car_heading, car_pos))
print(affine_transform_mat(obsv3, car_heading, car_pos))
