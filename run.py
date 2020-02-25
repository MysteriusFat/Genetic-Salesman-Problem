"""
Problem, you have traver for 10 citys and back to the city 1, but you dont want spend so much inn gasoline.
You star to thing how visited all citys in the lower distance,
"""

import pygame
import math
import random

from Simulation.classes.information import Info
from Simulation.classes.city import City
from Simulation.classes.people import People

from Simulation import Draw

pygame.init()
from Simulation import screen
screen.fill((30,30,30))

colors = [
    (205, 97, 85),(175, 122, 197),
    (84, 153, 199),(72, 201, 176),
    (82, 190, 128),(244, 208, 63),
    (220, 118, 51),(202, 207, 210),
    (153, 163, 164),(86, 101, 115)
]

citys = []
peoples = []
population = 100

for i in range(len(colors)):
    x = int(math.cos( i/len(colors) * math.pi*2 )*200 + 900/2 + 120 )
    y = int(math.sin( i/len(colors) * math.pi*2 )*200 + 600/2)
    citys.append( City(x, y, colors[i]) )

for i in range( population ):
    peoples.append( People(random.sample([x for x in range(0,len(colors))], len(colors) )) )

info = Info( 0, 0, population )
info.Draw()

min = 0
run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for people in peoples:
        x = people.Run( citys )
        if x > min:
            min = x
            best_p = people

    for i, people in enumerate(peoples):
        x = random.randrange(0, len(peoples), 1)
        peoples[i] = people.Reproduction( peoples[x] )
        peoples[i].Mutated()

    info.best = min
    info.generation += 1
    Draw(info, citys, best_p)

pygame.quit()
