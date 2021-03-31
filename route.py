import numpy as np
import random
import math
import map

MUTATION_RATE = 0.1

class Route():
    def __init__(self, n, map):
        self.num_of_cities = n
        self.fitness = 0
        self.distance = 0
        self.map = map
        self.path = self.random_path()
    
    def random_path():
        return np.random.permutation(self.num_of_cities)

    def calcDistance():
        for i in range(self.num_of_cities-1):
            self.distance += map.distances[self.path[i]][self.path[i+1]]

    def calcFitness():
        self.fitness = 1/self.distance

    def mutate(): #switch position of two random cities
        



    
