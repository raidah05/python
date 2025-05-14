import pygame
pygame.init()
a , b = 500,500
display_surface = pygame.display.set_mode((a,b))

pygame.display.set_caption("Adding image and background image")
surface = pygame.Surface((100,200))

background_img = pygame.transform.scale(pygame.image.load('E:\CODINGAL testbasedcoding\python\pygame image\background.png').convert(),(a,b))

penguine_img = pygame.transform.scale(pygame.image.load('penguine.jpeg').convert_alpha(),(200,200))

penguine_rect = penguine_img.get_rect(center =(a//2,b//2-30))

text = pygame.font.Font(None,35).render("Hello world",True, pygame.color('black'))
text_rect = text.get_rect(center =(a//2,b//2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.blit(background_img,(0,0))     
        display_surface.blit(penguine_img,penguine_rect)
        display_surface.blit(text,text_rect)


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ =='__main__':
    game_loop()