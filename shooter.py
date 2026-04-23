import pygame
import random
import sys 

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter 2D")

clock = pygame.time.Clock()

#Colores
WHITE = (255,255,255)
RED = (255, 60,60)
GREEN = (60,255,60)
BLACK = (20,20,20)

#Jugador
player = pygame.Rect(370, 500, 60, 40)
player_speed = 6

#Balas 
bullets = []
bullet_speed = 8

#Enemigos 
enemies = []
enemy_speed = 3 

SPAWN_ENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWN_ENEMY, 1000)

score = 0
font = pygame.font.SysFont(None, 36)

#Loop Principal
while True:
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SPAWN_ENEMY:
            x = random.randint(0, WIDTH-40)
            enemies.append(pygame.Rect(x, -40, 40, 40))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(player.centerx-5, player.y, 10, 20)
                )
    #Movimiento del jugador
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.RIGHT] and player.right < WIDTH:
        player.x += player_speed
    
    #Movimiento de las balas
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)
    
    #Movimiento de los enemigos
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            
    #Colisiones
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullet.remove(bullet)
                score += 1
                break
    #Dibujos
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, GREEN, player)
    
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
        
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
        
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10,10))
    
    pygame.display.flip()
    clock.tick