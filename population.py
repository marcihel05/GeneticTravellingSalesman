import numpy as np
import random
import math
from route import Route
from graph import Map
import matplotlib.pyplot as plt

class  Population():
    def __init__(self, n, m, map):
        self.map = map
        self.num_of_routes = n
        self.num_of_cities = m
        self.routes = []
        for i in range(n):
            self.routes.append(Route(m,map))
        self.fitness = 0
        self.best_distance_in_generation = []
        self.best_route = ""
        self.num_of_generation = 1

    def calcFitness(self):
        self.fitness = 0
        for route in self.routes:
            route.calcFitness()
            self.fitness += route.fitness

    def find_best_route(self):
        best_route = self.routes[0]
        for route in self.routes:
            if best_route.fitness > route.fitness:
                best_route = route
        self.best_distance_in_generation.append(best_route.distance)
        self.best_route = best_route

    
    def geneticAlgorithm(self):
        self.calcFitness()
        self.find_best_route()
        new_routes = [self.best_route]
        for i in range(self.num_of_routes):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = self.crossover(parent1, parent2)
            child.mutate()
            print(child.path)
            new_routes.append(child)
        self.routes = new_routes
        self.fitness = 0
        self.num_of_generation += 1

    
    def crossover(self, parent1, parent2):
        child = Route(self.num_of_cities, self.map)
        gene1 = random.randint(0, self.num_of_cities)
        gene2 = random.randint(0, self.num_of_cities)

        start = min(gene1, gene2)
        end = max(gene1, gene2) + 1

        child.path[start:end] = parent1.path[start:end]
        i = j = 0
        while i < self.num_of_cities and j < self.num_of_cities:
            if start <= i < end:
                i += 1
            else:
                while parent2.path[j] in child.path and j < self.num_of_cities - 1:
                    j += 1
                child.path[i] = parent2.path[j]
                i += 1
        return child
        

    def select_parent(self):
        rnd = random.uniform(0, self.fitness)
        suma = 0
        for route in self.routes:
            suma += route.fitness
            if suma >= rnd:
                return route

    #def draw_distance_over_iterations():


    

        
