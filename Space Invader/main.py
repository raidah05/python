import math
import pygame 
import random

screen_width = 800
screen_height = 500
player_start_X = 370
player_start_Y = 380
enemy_start_y_min = 50 
enemy_start_y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 40
bullet_speed_Y = 10
collision_dis = 27 


pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('backgrouund.png')
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('main.png')
playerx = player_start_X
playery = player_start_Y
playerX_change = 0 


enemyimg = []
enemy_x = []
enemy_Y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,screen_width-64))
    enemy_Y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_X)
    enemy_y_change.append(enemy_speed_Y)

bulletimg = pygame.image.load('bullet.png')
bullet_x = 0 
bullet_x_change = 0 
bullet_y = player_start_Y
bullet_y_change = bullet_speed_Y
bullet_state = "Ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
overfont = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text = overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletimg,(x+16,y+10))

def iscollision(enemy_x,enemy_Y,bullet_x,bullet_y):
    distance = math.sqrt((enemy_x-bullet_x)**2 + (enemy_Y-bullet_y)**2)
    return distance< collision_dis

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = -5
            if event.type == pygame.K_RIGHT:
                playerX_change = 5
            if event.type == pygame.K_SPACE and bullet_state == "Ready":
                bullet_x = playerx
                fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT , pygame.K_RIGHT]:
            playerX_change = 0 

        
playerx += playerX_change
playerx = max(0,min(playerx , screen_width-64))

for i in range(num_of_enemies):
    if enemy_Y[i] > 340:
        for j in range(num_of_enemies):
            enemy_Y[j] = 2000
        game_over_text()
        break
    enemy_x[i] += enemy_x_change[i]
    if enemy_x[i]<= 0 or enemy_x[i]>= screen_width-64:
        enemy_x_change[i] *= -1
        enemy_Y[i] +=enemy_y_change[i]
    if iscollision(enemy_x[i],enemy_Y[i], bullet_x,bullet_y):
        bullet_y = player_start_Y
        bullet_state = "Ready"
        score_value +=1
        enemy_x[i] = random.randint(0, screen_width-64)
        enemy_Y[i] = random.randint(enemy_start_y_min,enemy_start_y_max)

    enemy(enemy_x[i], enemy_Y[i], i)


if bullet_y<= 0:
    bullet_y = player_start_Y
    bullet_state = "Ready"  
elif bullet_state == "Fire":
    fire_bullet(bullet_x,bullet_y)
    bullet_y -=bullet_y_change

player(playerx,playery)
show_score(textX,textY)
pygame.display.update()
