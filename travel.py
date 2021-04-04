import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from population import Population
from route import Route
from graph import Map
import math
import time
import numpy as np
from settings import *


FPS = 30

pygame.font.init()
FONT = pygame.font.SysFont("monospace", 25)


def draw_window(win, population, i):
    win.fill(BLACK)
    population.draw_path(win)
    gen_text = FONT.render('Current generation: ' + str(i), 1, WHITE)
    dist_text = FONT.render('Shortest distance: ' + str(population.best_route.distance), 1, WHITE)
    first_dist_text = FONT.render('Starting distance: ' + str(population.best_distance_in_generation[0]), 1, WHITE)
    win.blit(gen_text, (500, 10))
    win.blit(dist_text, (500, 60))
    win.blit(first_dist_text, (500, 35))
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Travelling Salesman Problem')
    clock = pygame.time.Clock()
    graph = Map(NUM_OF_CITIES, 'load')
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
    while run:
        draw_window(win, population, i)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    print(population.best_distance_in_generation[0])
    print(population.best_route.distance)
    population.save_path()
    

main()

    