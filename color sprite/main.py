import pygame
import random

pygame.init()

sprite_colorchange_event = pygame.USEREVENT + 1
background_colorchange_event = pygame.USEREVENT + 2

blue = pygame.Color('blue')
dark_blue = pygame.Color('dark blue')
sage_green = pygame.Color('green')


yellow = pygame.Color('yellow')
magenta = pygame.Color('magenta')
pink = pygame.Color('pink')
white = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary = False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundary= True
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            boundary= True
        if boundary:
            pygame.event.post(pygame.event.Event(sprite_colorchange_event))
            pygame.event.post(pygame.event.Event(background_colorchange_event))

    def change_color(self):
        self.image.fill(random.choice([yellow,magenta,pink,white]))

def background_color():
    global bg_color
    bg_color = random.choice([blue,dark_blue,sage_green])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('colorful bounce')
bg_color= blue
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_colorchange_event:
            sp1.change_color()
        elif event.type == background_colorchange_event:
            background_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()
    



