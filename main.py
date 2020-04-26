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

# 무한 루프
while not done:
    clock.tick(10)

    # 게임 이벤트 처리
    for event in pygame.event.get():
        # 'KEYDOWN' 이벤트 처리
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
        # 'QUIT' 이벤트 처리
        elif event.type ==pygame.QUIT:
            done = True

        # 'buttons' 처리
        for btn in buttons:
            if btn == 'right':
                x = x + 10
            elif btn == 'left':
                x = x - 10

        screen.fill(WHITE)

        # 그림 그리는 명령 입력
        pygame.draw.line(screen, RED, [0, 0], [800, 450], 1)
        pygame.draw.lines(screen, BLUE, False, [[100, 100], [200, 100], [200, 200], [100, 200]], 3)
        pygame.draw.rect(screen, GREEN, [x, y, 50, 50], 0)
        pygame.draw.polygon(screen, RED, [[400, 400], [500, 400], [450, 300]], 5)

        # 실제 그림을 그리는 단계
        pygame.display.flip()

# 게임 종료 처리
pygame.quit()

