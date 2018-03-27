import numpy as np
import random

class Network(object):

    def __init__(self, sizes):
        self.layers = []
        self.synapses = []
        for i in sizes:
            self.layers.append(np.array([0 for _ in range(i)])) # 1 x i matrix
        for i in range(len(sizes)-1): # append sizes[i] x sizes[i] matrix
            self.synapses.append(np.array([[random.uniform(-1,1) for _ in range(sizes[i+1])] for _ in range(sizes[i])]))

    def prt(self):
        print(str(self.layers) + " ---- " + str(self.synapses))

    def run(self, in_val):
        for i in range(len(in_val)):
            self.layers[0][i] = in_val[i] # set input values
        for i in range(len(self.synapses)): # multiply layer by synapse layer
            self.layers[i+1] = self.layers[i]@self.synapses[i]
