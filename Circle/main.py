import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
screen.fill('white')
pink = ('light pink')

pygame.draw.circle(screen,pink,(300,300),50)
pygame.draw.circle(screen,pink,(100,100),50,3)
pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False

pygame.quit()