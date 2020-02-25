import pygame

from Simulation import screen

class Info():
    def __init__( self, x, y, population ):
        self.x = x
        self.y = y
        self.height = 600
        self.width = 300
        self.color = (20,20,20)
        self.font_color = (229, 231, 233)
        self.font_title = pygame.font.Font("freesansbold.ttf", 25 )
        self.font_normal = pygame.font.Font("freesansbold.ttf", 20 )

        self.generation = 0
        self.population = population
        self.best = 0

    def Draw( self ):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
        title_ = self.font_title.render("Genetic Algorithm", True, self.font_color )
        pop_ = self.font_normal.render("Population: {}".format(self.population ), True, self.font_color )
        gen_ = self.font_normal.render("Generation: {}".format(self.generation), True, self.font_color )
        best = self.font_normal.render("Shortest: {}".format(self.best), True, self.font_color )

        screen.blit( title_, (15,20) )
        screen.blit( pop_, (15,80) )
        screen.blit( gen_, (15,110) )
        screen.blit( best, (15,140) )
