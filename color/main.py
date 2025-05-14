import pygame

def main():
    pygame.init()
    a,b=400,500
    screen = pygame.display.set_mode((a,b))
    pygame.display.set_caption("Color changing sprite")

    color={
        'red':pygame.Color('red'),
        'pink':pygame.Color('pink'),
        'blue':pygame.Color('blue'),
        'green':pygame.Color('green'),
        'white':pygame.Color('white')
    }
    current_color = color['white']
    x,y =(30,30)
    width,height =(60,60)

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done= True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_RIGHT]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3

        x = min(max(0,x),a-width)
        y = min(max(0,y),b-height)

        if x == 0: current_color=color['blue']
        elif x == a - width : current_color= color['pink']
        elif y == 0: current_color = color['red']
        elif y == b - height : current_color= color['green']
        else:
            current_color = color['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, width, height))

        pygame.display.flip()
        clock.tick(90)

pygame.quit()

if __name__ =='__main__':
    main()