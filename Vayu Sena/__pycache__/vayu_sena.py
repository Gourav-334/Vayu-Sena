# Formalities
import pygame
import random
import math
from pygame import mixer
from main_menu import menu
pygame.init()

# Resolution(s)
screen = pygame.display.set_mode((1100, 700))
menu = pygame.image.load('menu.png')
pygame.display.set_caption("Vayu Sena")
logo = pygame.image.load('logo.png')
pygame.display.set_icon(logo)

# Game Over Design
game_over = pygame.image.load('game_over.png')
game_overX = 400
game_overY = 400
game_overXv = 0
game_overYv = 0
screen.blit(game_over, (game_overX, game_overY))

# Appreciation Board
brutal = pygame.image.load('brutal.png')
brutalX = 400
brutalY = -100
brutalXv = 0
brutalYv = 2
def brutal_pos():
    screen.blit(brutal, (brutalX, brutalY))

# Player Identity
player = pygame.image.load('player.png')
playerX = 400
playerY = 400
playerXv = 0
playerYv = 0
player_axis = (playerX, playerY)
def player_pos():
    screen.blit(player, (playerX, playerY))

# Bullet Identity
bullet = pygame.image.load('bullet.png')
bulletX = 570
bulletY = 565
bulletXv = 0
bulletYv = 0
def bullet_pos():
    screen.blit(bullet, (bulletX, bulletY))

# Multiple Enemies Setting
enemy = []
enemyX = []
enemyY = []
enemyXv = []
enemyYv = []
num_enemies = 6

# Enemy Identity
enemy = pygame.image.load('enemy.png')
enemyX = random.randint(0,500)
enemyY = 0
enemyXv = 1
enemyYv = 0
enemy_axis = (enemyX, enemyY)
def enemy_pos():                                                                       
    screen.blit(enemy, (enemyX, enemyY))

# Player Damage Identity
player_low = pygame.image.load('player_low.png')
player_lowX = playerX
player_lowY = playerY + 2000
player_lowXv = playerXv
player_lowYv = playerYv
player_low_axis = (player_lowX, player_lowY)
def player_low_pos():
    screen.blit(player_low, (player_lowX, player_lowY))

# Enemy Damage Identity
enemy_low = pygame.image.load('enemy_low.png')
enemy_lowX = enemyX
enemy_lowY = enemyY - 2000
enemy_lowXv = enemyXv
enemy_lowYv = enemyYv
enemy_low_axis = (enemy_lowX, enemy_lowY)
def enemy_low_pos():
    screen.blit(enemy_low, (enemy_low_axis))

# Health COORDINATES
healthX = 0
healthY = 639
health_axis = (healthX, healthY)

# Health1 Identity
health1 = pygame.image.load('health1.png')
health1_axis = (healthX, healthY)
def health1_pos():
    screen.blit(health1, (health1_axis))

# Health2 Identity
health2 = pygame.image.load('health2.png')
health2_axis = (healthX, healthY)
def health2_pos():
    screen.blit(health2, (health2_axis))

# Health3 Identity
health3 = pygame.image.load('health3.png')
health3_axis = (healthX, healthY)
def health3_pos():
    screen.blit(health3, (health3_axis))

# Health4 Identity
health4 = pygame.image.load('health4.png')
health4_axis = (healthX, healthY)
def health4_pos():
    screen.blit(health4, (health4_axis))

# Health5 Identity
health5 = pygame.image.load('health5.png')
health5_axis = (healthX, healthY)
def health5_pos():
    screen.blit(health5, (health5_axis))

# Health6 Identity
health6 = pygame.image.load('health6.png')
health6_axis = (healthX, healthY)
def health6_pos():
    screen.blit(health6, (health6_axis))

# Health7 Identity
health7 = pygame.image.load('health7.png')
health7_axis = (healthX, healthY)
def health7_pos():
    screen.blit(health7, (health7_axis))

# Target Identity
target = pygame.image.load('crosshair.png')
targetX = 510
targetY = 348
targetXv = 0
targetYv = 0
target_axis = (targetX, targetY)
def target_pos():
    screen.blit(target, (targetX, targetY))

# Cloud1 Identity
cloud1 = pygame.image.load('cloud1.png')
cloud1X = random.randint(0,800)
cloud1Y = random.randint(0,600)
cloud1Yv = 0.05
def cloud1_pos():                                                                   
    screen.blit(cloud1, (cloud1X, cloud1Y))

# Cloud2 Identity
cloud2 = pygame.image.load('cloud2.png')
cloud2X = random.randint(0,800)
cloud2Y = random.randint(0,600)
cloud2Yv = 0.05
def cloud2_pos():                                                               
    screen.blit(cloud2, (cloud2X, cloud2Y))

# Cloud3 Identity
cloud3 = pygame.image.load('cloud3.png')
cloud3X = random.randint(0,800)
cloud3Y = random.randint(0,600)
cloud3Yv = 0.05
def cloud3_pos():                                                           
    screen.blit(cloud3, (cloud3X, cloud3Y))

# Collision Area
collision_left = enemyX - 100
collision_right = enemyY + 100
collision_up = enemyY - 100
collision_down = enemyY + 100

collisionX = (collision_left, collision_right)
collisionY = (collision_up, collision_down)

# Visual Defining
pygame.display.update()
sky_blue = (0, 155, 255)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def score(x, y):
    score = font.render("AirKills: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

# Collision Detection
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 282:
        return True
    else:
        return False

# Setting Loops
running = True
while running:

    # Display
    screen.fill(sky_blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # Events after button(s) are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXv = -1.7
                targetXv = -1.7
                if bulletY == 565:
                    bulletXv = -1.7
                mixer.music.load('move.wav')
                mixer.music.play(-1)
                print('<---')
            if event.key == pygame.K_RIGHT:
                playerXv = 1.7
                targetXv = 1.7
                if bulletY == 565:
                    bulletXv = 1.7
                mixer.music.load('move.wav')
                mixer.music.play(-1)
                print('--->')
            if event.key == pygame.K_UP:
                targetYv = -1.5
                mixer.music.load('lock_alarm.wav')
                mixer.music.play(-1)
                print('Searching For Target...')
            if event.key == pygame.K_DOWN:
                targetYv = 1.5
                mixer.music.load('lock_alarm.wav')
                mixer.music.play(-1)
                print('Searching For Target...')
            if event.key == pygame.K_SPACE:
                if bulletY >= -34:
                    bulletXv = 0
                bulletYv = -20
                mixer.music.load('gun.wav')
                mixer.music.play() 
                print('One Round Fired!')

                if bulletX == enemyX - 100:
                    mixer.music.load('destroy.wav')
                    mixer.music.play()
                    enemyX = random.randint(0,500)
                    enemyY = random.randint(0,400)

        # Events after button(s) are released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXv = 0
                targetXv = 0
                bulletXv = 0
                mixer.music.load('engine.wav')
                mixer.music.play(-1)
                print('Static')
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                targetYv = 0
                mixer.music.load('engine.wav')
                mixer.music.play(-1)
                print('Search Completed!')

    # Collision Teaser
    def collision_detector():
        for x in range(collision_left, collision_right):
            if bulletX == x:
                print('X-Coordinates Matched!')
                enemyY += 2000
                mixer.music.load('damage.wav')
                mixer.music.play()

    # Cloud1 Mechanics
    cloud1Y += cloud1Yv  
    if cloud1Y <= 600:
        cloud1X = random.randint(0, 800)
        cloud1Y = random.randint(0, 600)
        cloud1Y += cloud1Yv

    # Cloud2 Mechanics
    cloud2Y += cloud2Yv  
    if cloud2Y <= 600:
        cloud2X = random.randint(0, 800)
        cloud2Y = random.randint(0, 600)
        cloud2Y += cloud2Yv

    # Cloud3 Mechanics
    cloud3Y += cloud3Yv  
    if cloud3Y <= 600:
        cloud3X = random.randint(0, 800)
        cloud3Y = random.randint(0, 600)
        cloud3Y += cloud3Yv

    # Foe Mechanics
    enemyX += enemyXv  
    if enemyX <= 0:
        enemyXv = 1
        enemyY += 100
    elif enemyX >= 799:
        enemyXv = -1
        enemyY += 100

    # Player Mechanics
    playerX += playerXv  
    if playerX <= -185:
        playerX = -185
    elif playerX >= 930:
        playerX = 930

    # Crosshair Mechanics
    targetX += targetXv
    if playerX == -185 or playerX == 930:
        targetXv = 0
    
    targetY += targetYv
    if targetY <= 0:
        targetY = 0
    elif targetY >= 650:
        targetY = 650
    elif playerXv == 0:
        targetXv = 0

    # Bullet Mechanics
    bulletY += bulletYv
    if bulletY <= -35 and playerXv == 0:
        bulletY = 565
        bulletYv = 0
        bulletXv = 0
        bulletX = playerX + 170

    elif bulletY <= -35 and playerXv != 0:
        bulletY = 565
        bulletYv = 0
        bulletXv = playerXv
        bulletX = playerX + 170

    elif playerX == -185 or playerX == 930:
        bulletXv = 0

    bulletX += bulletXv

    # inCollision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        score_value += 1
        mixer.music.load('destroy.wav')
        mixer.music.play()
        enemyX = random.randint(0,550)
        enemyY = 0
    
    # Weapon Navigation
    def navy():
        if bulletX == enemyX + 230:
            print('X-Coordinates Matching!')
        elif bulletX == enemyX + 20:
            print('Again!')
        elif bulletY == enemyY:
            print('Y-Coordinates Matching!')

    # Racing Performance Machine
    def rpm():
        for x in range(int(enemyX + 230), int(enemyX + 20)):
            if bulletX == x:
                print('Signals Recieved!')
                enemyY += 2000
                mixer.music.load('damage.wav')
                mixer.music.play()

    # Pilot Warning System
    crew = 0
    crew1 = 0
    crew2 = 0
    crew3 = 0
    crew4 = 0
    crew5 = 0
    crew6 = 0
    
    if crew == 0 and enemyY == 300:
        mixer.music.load('damage.wav')
        mixer.music.play()
        crew = 1
        health1_axis = (healthX + 1000, healthY + 1000)
        player = player_low
    if crew == 1 and enemyY == 300:
        mixer.music.load('damage.wav')
        mixer.music.play()
        crew = 2
        health2_axis = (healthX + 1000, healthY + 1000)
    if crew == 2 and enemyY == 300:
        mixer.music.load('damage.wav')
        mixer.music.play()
        crew = 3
        health3_axis = (healthX + 1000, healthY + 1000)
    if crew == 3 and enemyY == 300:
        mixer.music.load('damage.wav')
        mixer.music.play()
        crew = 4
        health4_axis = (healthX + 1000, healthY + 1000)

    # Hoarding (For Fixing Glitch)
    if health4_axis == (healthX + 1000, healthY + 1000):
        brutalY += brutalYv
        if brutalY == 800:
            brutalYv = 0
    
    if brutalY == 800 and enemyY >= 290:
        health5_axis = (5000, 5000)
        health6_axis = (5000, 5000)
        health7_axis = (5000, 5000)
        enemyX, enemyY = (5000, 5000)
        targetX, targetY = (5000, 5000)
        game_overY += game_overYv
        if brutalYv == 0:
            mixer.music.load('ending_opera.wav')
            mixer.music.play(-1)
        
    # Decorative Iffing
    game_overY += game_overYv
    
    # Calling Functions
    enemy_pos()
    enemy_low_pos ()
    bullet_pos()
    target_pos()
    player_pos()
    player_low_pos ()
    health7_pos()
    health6_pos()
    health5_pos()
    health4_pos()
    health3_pos()
    health2_pos()
    health1_pos()
    isCollision(enemyX, enemyY, bulletX, bulletY)
    score(textX, textY)
    brutal_pos()

    # Display Update
    pygame.display.update()
