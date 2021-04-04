import numpy as np
import random
import math
from settings import *

class Map():
    def __init__(self, n, option = 'random'):
        self.num_of_cities = n
        if option == 'random':
            self.xy = np.array([random.uniform(200, 600), random.uniform(200,600)] for i in range(n))
        if option == 'circle':
            self.xy = np.array([[math.cos(t), math.sin(t)]*250 + 400 for t in np.linspace(0, 2*math.pi, n)])
        if option == 'load':
            self.xy = self.load_from_file()
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
        mn =  -min(arr[:,0])
        for i in range(self.num_of_cities):
            arr[i][0] += mn
        for i in range(self.num_of_cities):
            arr[i] += 55
            arr[i] /= 7
        print(arr)
        return arr

                #NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin



        


        

