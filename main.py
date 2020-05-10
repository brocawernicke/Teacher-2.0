# 파이썬 게임 패키지 사용
import pygame
import os

# 색깔 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  게임 준비
pygame.init()
done = False
gameover = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,450])

bg = pygame.image.load(os.path.join('images', 'space_bg.jpg')).convert()
spaceship = pygame.image.load(os.path.join('images', 'spaceship.png')).convert_alpha()
enemy = pygame.image.load(os.path.join('images', 'enemy.png')).convert_alpha()
explosion = pygame.image.load(os.path.join('images', 'explosion.png')).convert_alpha()

buttons = []
x = 400
y = 220
x_direction = 0
y_direction = 0
x1 = 450
y1 = 220
x1_direction = 10
y1_direction = 10
x2 = 200
y2 = 120
x2_direction = 10
y2_direction = -10
x3 = 600
y3 = 320
x3_direction = -10
y3_direction = 10
score = 0
bgY = 0
bgY2 = -450

# 폰트 준비
font1 = pygame.font.SysFont("Arial", 72)
font2 = pygame.font.SysFont("Arial", 24)

# 무한 루프
while not done:
    clock.tick(30)

    # 게임 이벤트 처리
    for event in pygame.event.get():
        # 'QUIT' 이벤트 처리
        if event.type ==pygame.QUIT:
            #done = True
            pygame.quit()
            sys.exit()
        # 'KEYDOWN' 이벤트 처리
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]

        # 'buttons' 처리
        for btn in buttons:
            if btn == 'right':
                x_direction = 10
            elif btn == 'left':
                x_direction = -10

    # 배경화면 스크롤
    bgY += 3
    bgY2 += 3
    if bgY > 450:
        bgY = -450
    if bgY2 > 450:
        bgY2 = -450
    screen.blit(bg, (0, bgY))
    screen.blit(bg, (0, bgY2))
    #screen.blit(bg, pygame.rect.Rect(0,0, 800, 450))

    # Score 표시
    score += 1
    score_text = font2.render("score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

   # 물체 움직이기 (좌표 변경)
    x += x_direction
    y += y_direction
    x1 = x1 + x1_direction
    y1 = y1 + y1_direction
    x2 += x2_direction
    y2 += y2_direction
    x3 += x3_direction
    y3 += y3_direction

    # 벽에 부딪힘 처리
    if x > 780:
        x = 780
    if x < 0:
        x = 0
        
    if x1 > 800:
        x1_direction = -10
    if x1 < 0:
        x1_direction = 10
    if y1 > 450:
        y1_direction = -10
    if y1 < 0:
        y1_direction = 10

    if x2 > 800:
        x2_direction = -10
    if x2 < 0:
        x2_direction = 10
    if y2 > 450:
        y2_direction = -10
    if y2 < 0:
        y2_direction = 10

    if x3 > 800:
        x3_direction = -10
    if x3 < 0:
        x3_direction = 10
    if y3 > 450:
        y3_direction = -10
    if y3 < 0:
        y3_direction = 10

    # 그림 그리는 명령 입력
    screen.blit(spaceship, (x, y))
    screen.blit(enemy, (x1, y1))
    screen.blit(enemy, (x2, y2))
    screen.blit(enemy, (x3, y3))

    # 물체 충돌 처리
    if abs(x - x1) < 30 and abs(y - y1) < 30:
        gameover = True
    if abs(x - x2) < 30 and abs(y - y2) < 30:
        gameover = True
    if abs(x - x3) < 30 and abs(y - y3) < 30:
        gameover = True

    # Game Over
    if gameover == True:
        screen.blit(explosion, (x-50, y-50))
        text = font1.render("Game Over", True, WHITE)
        screen.blit(text, (400 - text.get_width() // 2, 240 - text.get_height()))

    # 실제 그림을 그리는 명령
    pygame.display.flip()
    #pygame.display.update()

    if gameover == True:
        pygame.time.delay(1000)
        score = 0
        x = 400
        y = 225
        x_direction = 0
        y_direction = 0
        gameover = False

pygame.time.delay(1000)

# 게임 화면 종료
pygame.quit()

