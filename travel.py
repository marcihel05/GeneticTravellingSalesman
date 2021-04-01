from population import Population
from route import Route
from graph import Map
import math

def main():
    num_of_cities = 50
    num_of_routes = 25
    num_of_generations = 10000
    graph = Map(num_of_cities)
    population = Population(num_of_routes, num_of_cities, graph)
    for i in range(num_of_generations):
        population.geneticAlgorithm()
        
    
   # print(population.best_route.path)
    print(population.best_distance_in_generation[0])
    for i in range(num_of_generations):
        if i % 250 == 0:
            print(population.best_distance_in_generation[i])
    print(population.best_route.distance)
    

main()

    