from population import Population
from route import Route
from graph import Map
import math

def main():
    num_of_cities = 50
    num_of_routes = 100
    num_of_generations = 500
    graph = Map(num_of_cities)
    population = Population(num_of_routes, num_of_cities, graph)
    new_dist = old_dist = 0
    #for i in range(num_of_generations):
    i = 1
    while True:
        population.geneticAlgorithm()
        print(i)
        i+=1
        new_dist = population.best_route.distance
        print(new_dist)
        if abs(new_dist-old_dist) < 10**(-5):
            break
        old_dist = new_dist
    print(population.best_route.distance)

main()

    