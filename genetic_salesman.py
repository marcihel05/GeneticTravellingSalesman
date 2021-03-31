import networkx as nx
import numpy as np
import random
import math

class Tour():
    def __init__(self, n):
        self.num_of_cities = n
        self.xy = np.zeros((n,2))
        for i in range(n):
            self.xy[i] = random.randint(0, 500), random.randint(0,500)
        self.distances = np.zeros((n,n))
        self.calculate_distances()


    def calculate_distances():
        for i in range(self.num_of_cities):
            p = self.xy[i]
            for j in range(self.num_of_cities):
                q = self.xy[j]
                self.distances[i][j] = math.dist(p,q)
    
    def draw_graph():

    def draw_coordinate():


        


        

