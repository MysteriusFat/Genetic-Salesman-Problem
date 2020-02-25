import pygame
import pygame.gfxdraw
import random
from Simulation import screen

class People():
    def __init__( self, list ):
        self.gen = list
        self.color = (229, 231, 233)
        self.mutated_change = 0.8
        self.crosover_change = 0.8

    def Run( self, citys ):
        self.dist = 0
        for i in range(len(self.gen)):
            if i == 9:
                self.dist += abs((citys[self.gen[i]].x + citys[0].x)**2  + (citys[self.gen[i]].y + citys[0].y)**2 )
            else:
                self.dist += abs((citys[self.gen[i]].x + citys[self.gen[i+1]].x)**2  + (citys[self.gen[i]].y + citys[self.gen[i+1]].y)**2 )
        self.dist += abs((citys[self.gen[0]].x + citys[self.gen[-1]].x)**2  + (citys[self.gen[0]].y + citys[self.gen[-1]].y)**2 )
        return self.dist

    def Draw( self, citys ):
        for i in range(len(self.gen)):
            if i == 9:
                pygame.gfxdraw.line(screen, citys[self.gen[i]].x, citys[self.gen[i]].y,citys[0].x, citys[0].y, self.color )
            else:
                pygame.gfxdraw.line(screen, citys[self.gen[i]].x, citys[self.gen[i]].y,citys[self.gen[i+1]].x, citys[self.gen[i+1]].y, self.color )
        pygame.gfxdraw.line(screen, citys[self.gen[0]].x, citys[self.gen[0]].y,citys[self.gen[-1]].x, citys[self.gen[-1]].y, self.color )

    def Mutated( self ):
        x = random.randint(0,100)/100
        if self.mutated_change < x:
            x = random.randrange(0, len(self.gen), 1)
            y = random.randrange(0, len(self.gen), 1)

            aux = self.gen[x]
            self.gen[x] = self.gen[y]
            self.gen[y] = aux

    def Reproduction( self, other_guy ):
        change = random.randint(0,100)/100
        new_gen = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        if change < self.crosover_change:
            x = random.randrange(0, len(other_guy.gen)-1, 1)
            y = random.randrange(1, len(other_guy.gen)-x, 1)
            for i in range( y ):
                new_gen[i+x] = other_guy.gen[i+x]
            cont = x+y
            for i in range(x+y, len(new_gen)):
                if self.gen[i] not in new_gen:
                    new_gen[cont] = self.gen[i]
                    cont += 1
                    if cont >= len(new_gen):
                        cont = 0
            for i in range(0, len(new_gen)):
                if self.gen[i] not in new_gen:
                    new_gen[cont] = self.gen[i]
                    cont += 1
                    if cont >= len(new_gen):
                        cont = 0
            return People( new_gen )
        return People( self.gen )
