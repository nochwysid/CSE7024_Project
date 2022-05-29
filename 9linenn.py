#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:43:06 2019

@author: iridium
"""
import numpy as np
training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = np.array([[0, 1, 1, 0]]).T
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1
for iteration in range(10000):
    output = 1 / (1 + np.exp(-(np.dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += np.dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
print( 'Toy NN result', 1 / (1 + np.exp(-(np.dot(np.array([1, 0, 0]), synaptic_weights)))) )