import numpy as np
import random
import math
import route
import map
import matplotlib.pyplot as plt

class  Population():
    def __init__(self, n, m, map):
        self.map = map
        self.num_of_routes = n
        self.num_of_cities = m
        self.routes = [Route(m, map)]*n
        self.fitness = 0
        self.best_distance_in_generation = []
        self.best_route = ""

    def calcFitness():
        for i in range(self.num_of_routes):
            self.routes[i].calcFitness
            self.fitness += routes[i].fitness

    def find_best_route():
        best_route = self.routes[0]
        for route in self.routes:
            if best_route.fitness > route.fitness:
                best_route = route
        self.best_distance_in_generation.append(best_route.distance)
        self.best_route = best_route

    
    def genetic_algorithm():
        self.calcFitness()
        self.find_best_route()
        new_routes = [self.best_route]
        for i in range(self.num_of_routes):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = self.crossover(parent1, parent2)
            child.mutate()
            new_routes.append(child)
        self.routes = new_routes
        self.fitness = 0

    
    def crossover(parent1, parent2):
        child = Route(self.num_of_cities, self.map)
        gene1 = random.randint(0, self.num_of_cities)
        gene2 = random.randint(0, self.num_of_cities)

        start = min(gene1, gene2)
        end = max(gene1, gene2) + 1

        child.path[start:end] = parent1.path[start:end]
        i = 0
        for gene in parent2.path:
            if gene not in child.path:
                child.path[i] = gene
                i += 1
        return child

    def select_parent():
        rand = random.randint(0, self.fitness)
        sum = 0
        for i in range(self.num_of_routes):
            sum += self.routes[i].fitness
            if sum >= rand:
                return self.routes[i]

    def draw_distance_over_iterations():


    

        
