import numpy as np
import random
import math
from route import Route
from graph import Map
import matplotlib.pyplot as plt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)

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
            if best_route.fitness < route.fitness:
                best_route = route
        self.best_distance_in_generation.append(best_route.distance)
        self.best_route = best_route.clone()
        self.best_route.distance = best_route.distance

    
    def geneticAlgorithm(self):
        self.calcFitness()
        self.find_best_route()
        new_routes = [self.best_route.clone()]
        for i in range(self.num_of_routes-1):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = self.crossover(parent1, parent2)
            child.mutate()
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
        child.path[:start] = child.path[end:] = -1
       

        for gene in parent2.path:
            if gene not in child.path:
                for i in range(self.num_of_cities):
                    if child.path[i] == -1:
                        child.path[i] = gene
                        break
        return child
        


    def select_parent(self):
        rnd = random.uniform(0, self.fitness)
        suma = 0
        for route in self.routes:
            suma += route.fitness
        suma = 0
        for route in self.routes:
            suma += route.fitness
            if suma >= rnd:
                return route

    def draw_distance_over_iterations(self):
        fig, ax = plt.subplots()
        ax.set_title('Distance over generations')
        ax.set_xlabel('Generation')
        ax.set_ylabel('Distance')
        x = np.arange(1, self.num_of_generations+1)
        ax.plot(x, self.best_distance_in_generation)
        fig

    def draw_path(self, win):
        for i in range(self.num_of_cities-1):
            pygame.draw.line(win, WHITE, self.map.xy[self.best_route.path[i]]*4, self.map.xy[self.best_route.path[i+1]]*4)
        pygame.draw.line(win, WHITE, self.map.xy[self.best_route.path[0]]*4, self.map.xy[self.best_route.path[-1]]*4)
        for i in range(self.num_of_cities):
            pygame.draw.circle(win, YELLOW, self.map.xy[i]*4, 5)

    #def save_path(self):
        


        
