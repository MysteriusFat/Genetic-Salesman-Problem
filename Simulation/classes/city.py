import pygame
import pygame.gfxdraw
from Simulation import screen
import math

class City():
    def __init__( self, x, y, color ):
        self.x = x
        self.y = y
        self.color = color
        self.raduis = 8

    def Draw( self ):
        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.raduis, self.color )
    
