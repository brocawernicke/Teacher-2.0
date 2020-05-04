# 파이썬 게임 패키지 사용
import pygame

# 색깔 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  게임 준비
pygame.init()
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,450])
buttons = []
x = 400
y = 225
x_direction = 10
y_direction = 10
x2 = 200
y2 = 125
x2_direction = 10
y2_direction = -10
x3 = 600
y3 = 325
x3_direction = -10
y3_direction = 10

screen.fill(WHITE)

# 무한 루프
while not done:
    clock.tick(100)

    # 게임 이벤트 처리
    for event in pygame.event.get():
        # 'QUIT' 이벤트 처리
        if event.type ==pygame.QUIT:
            done = True

    screen.fill(WHITE)

   # 물체 움직이기 (좌표 변경)
    x = x + x_direction
    y = y + y_direction
    x2 += x2_direction
    y2 += y2_direction
    x3 += x3_direction
    y3 += y3_direction

    # 벽에 부딪힘 처리
    if x > 800:
        x_direction = -10
    if x < 0:
        x_direction = 10
    if y > 450:
        y_direction = -10
    if y < 0:
        y_direction = 10

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
    pygame.draw.circle(screen, BLUE, [x, y], 20)
    pygame.draw.circle(screen, GREEN, [x2, y2], 20)
    pygame.draw.circle(screen, RED, [x3, y3], 20)

    # 실제 그림을 그리는 단계
    pygame.display.flip()

# 게임 종료 처리
pygame.quit()