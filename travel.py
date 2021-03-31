import population
import route
import map

def main():
    num_of_cities = 50
    num_of_routes = 100
    map = Map(num_of_cities)
    population = Population(num_of_routes, num_of_cities, map)
    
    