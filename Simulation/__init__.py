import pygame

size = [900, 600]
screen  = pygame.display.set_mode( size )

def Draw( info, citys, best_p ):

    pygame.draw.rect( screen,(30,30,30), [250,0, 650,600 ]  )
    info.Draw()
    best_p.Draw( citys )
    for city in citys:
        city.Draw()

    pygame.display.flip()
