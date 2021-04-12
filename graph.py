import numpy as np
import random
import math
from settings import *

class Map():
    def __init__(self, n, option = 'random'):
        self.num_of_cities = n
        if option == 'random':
            self.xy = np.array([[random.uniform(200, 700), random.uniform(200,700)] for i in range(n)])
            self.draw_xy = self.xy
        if option == 'circle':
            self.xy = np.array([[math.cos(t), math.sin(t)] for t in np.linspace(0, 2*math.pi, n)])
            self.draw_xy = np.array([[math.cos(t)*250 + 400, math.sin(t)*250 + 400] for t in np.linspace(0, 2*math.pi, n)])
        if option == 'load':
            self.xy = self.load_from_file()
            self.draw_xy = self.xy
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        distances = np.empty((self.num_of_cities, self.num_of_cities))
        for i in range(self.num_of_cities):
            p = self.xy[i]
            for j in range(self.num_of_cities):
                q = self.xy[j]
                distances[i][j] = math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
        return distances
    
    def load_from_file(self):
        arr = np.loadtxt(FILE)
        return arr



        


        

