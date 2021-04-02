import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from population import Population
from route import Route
from graph import Map
import math
import time


WIN_WIDTH = 1200
WIN_HEIGHT = 800

NUM_OF_CITIES = 50
NUM_OF_ROUTES = 25
NUM_OF_GENERATIONS = 50000

FPS = 10

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)


pygame.font.init()
FONT = pygame.font.SysFont("monospace", 25)


def draw_window(win, population, i):
    win.fill(BLACK)
    population.draw_path(win)
    gen_text = FONT.render('Current generation: ' + str(i), 1, WHITE)
    dist_text = FONT.render('Shortest distance: ' + str(population.best_route.distance), 1, WHITE)
    win.blit(gen_text, (500, 10))
    win.blit(dist_text, (500, 30))
    pygame.display.update()



def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Travelling Salesman Problem')
    clock = pygame.time.Clock()
    graph = Map(NUM_OF_CITIES)
    population = Population(NUM_OF_ROUTES, NUM_OF_CITIES, graph)
    run = True
    i = 0
    while i < NUM_OF_GENERATIONS and run:
        clock.tick(FPS)
        for event in pygame.event.get():
     	    if event.type == pygame.QUIT:
                run = False
        population.geneticAlgorithm()
        i +=1
        draw_window(win, population, i)
    print(population.best_distance_in_generation[0])
    print(population.best_route.distance)
    

main()

    