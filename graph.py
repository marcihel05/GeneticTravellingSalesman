import networkx as nx
import numpy as np
import random
import math
import matplotlib.pyplot as plt

class Map():
    def __init__(self, n):
        self.num_of_cities = n
        self.xy = np.empty((n,2))
        for i in range(n):
            self.xy[i] = random.randint(0, 100), random.randint(0,100)
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        distances = np.empty((self.num_of_cities, self.num_of_cities))
        for i in range(self.num_of_cities):
            p = self.xy[i]
            for j in range(self.num_of_cities):
                q = self.xy[j]
                distances[i][j] = math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
        return distances
    
    #def draw_graph():

    def draw_coordinate():
        fig, ax = plt.subplot()
        ax.set_title('Cities')
        ax.plt.scatter(self.xy[:,0], self.xy[:, 1])


        


        

