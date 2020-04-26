# 파이썬 게임 패키지 로딩
import pygame

# 편의를 위해 컬러 상수 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 게임 코딩 시작을 위한 초기화
pygame.init()
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,450])

# 무한 루프
while not done:
    clock.tick(10)

    # (pygame event)* 처리
    for event in pygame.event.get():
        # 종료 이벤트(quit event) 처리
        if event.type == pygame.QUIT:
            done = True

        screen.fill(WHITE)

        # (가상 화면에) 그림을 그리는 명령 입력
        pygame.draw.circle(screen, RED, [400, 225], 50, 3)
        pygame.draw.line(screen, RED, [0, 0], [800, 450], 1)
        pygame.draw.lines(screen, BLUE, False, [[100, 100], [200, 100], [200, 200], [100, 200]], 3)
        pygame.draw.rect(screen, GREEN, [400, 100, 50, 50], 0)
        pygame.draw.polygon(screen, RED, [[400, 400], [500, 400], [450, 300]], 5)

        # PC 화면에 그림을 그리라고 하는 최종 명령
        pygame.display.flip()

# 게임 종료 처리
pygame.quit()
