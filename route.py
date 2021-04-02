import numpy as np
import random
import math
import graph
import pandas as pd

MUTATION_RATE = 0.1

class Route():
    def __init__(self, n, graph):
        self.num_of_cities = n
        self.fitness = 0
        self.distance = 0
        self.map = graph
        self.path = np.random.permutation(self.num_of_cities)

    def calcDistance(self):
        for i in range(self.num_of_cities-1):
            self.distance += self.map.distances[self.path[i]][self.path[i+1]]
        self.distance += self.map.distances[self.path[0]][self.path[self.num_of_cities-1]]

    def calcFitness(self):
        self.calcDistance()
        self.fitness = 1/self.distance * 1000

    def mutate(self): 
        for i in range(self.num_of_cities):
            if random.random() < MUTATION_RATE:
                j = random.randrange(0, self.num_of_cities)
                self.path[i], self.path[j] = self.path[j], self.path[i]

    def clone(self):
        new_route = Route(self.num_of_cities, self.map)
        new_route.path = self.path
        return new_route
        



    
