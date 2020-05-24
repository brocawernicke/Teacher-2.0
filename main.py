'''
References:
  https://techwithtim.net/tutorials/game-development-with-python/side-scroller-pygame/background/
  https://opengameart.org/content/9-explosion-sounds
  https://devnauts.tistory.com/61
'''
# 게임 패키지 사용
import os
import pygame

# 색깔 상수 지정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  게임 변수 초기화
done = False
gameover = False

# 게임 준비
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,450])
bg = pygame.image.load(os.path.join('images', 'space_bg.jpg')).convert()
spaceship = pygame.image.load(os.path.join('images', 'spaceship.png')).convert_alpha()
explosion = pygame.image.load(os.path.join('images', 'explosion.png')).convert_alpha()
enemy = pygame.image.load(os.path.join('images', 'enemy.png')).convert_alpha()
enemy2 = pygame.transform.scale(enemy, (100, 100))

class Player(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.x_step = 0
        self.y_step = 0
        self.img = pygame.image.load(os.path.join('images', img)).convert_alpha()
    def update(self, screen, x_step, y_step):
        self.x_step = x_step
        self.y_step = y_step
        self.x += self.x_step
        self.y += self.y_step
        screen.blit(self.img, (self.x, self.y))
    def collisionDetection(self, object):
        return True

class Enemy(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.x_step = 0
        self.y_step = 0
        self.img = pygame.image.load(os.path.join('images', img)).convert_alpha()
    def update(self, screen, x_step, y_step):
        self.x_step = x_step
        self.y_step = y_step
        self.x += self.x_step
        self.y += self.y_step
        screen.blit(self.img, (self.x, self.y))
    def getX(self):
        return self.x
    def getY(self):
        return self.y

# class로 변경 진행 중
player = Player(400, 125, 'spaceship.png')
enemy10 = Enemy(100, 100, 'enemy.png')

# 각종 변수 초기화
score = 0
buttons = []

# player 초기 위치 및 속도
player_x = 400
player_y = 220
player_x_speed = 0
player_y_speed = 0

# enemy 초기 위치 및 속도
enemy_x = [450, 200, 600]
enemy_y = [220, 120, 320]
enemy_x_speed = [10, 10, -10]
enemy_y_speed = [10, -10, 10]
num_of_enemy = 3

# 초기 배경 좌표
bgY = 0
bgY2 = -450

# 폰트 준비
font1 = pygame.font.SysFont("Arial", 72)
font2 = pygame.font.SysFont("Arial", 24)

# BGM - download from https://opengameart.org/
pygame.mixer.music.load(os.path.join('sound', 'bgm.mp3'))
pygame.mixer.music.play(-1, 0)
soundObj = pygame.mixer.Sound(os.path.join('sound', 'explosion.wav'))

# 무한 루프
while not done:
    clock.tick(30) #FPS

    # 1) 이벤트 처리
    for event in pygame.event.get():
        # 'QUIT' 이벤트 처리
        if event.type ==pygame.QUIT:
            #done = True
            pygame.quit()
            os.sys.exit()
        # 'KEYDOWN' 이벤트 처리
        if gameover == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_x_speed = 10
                elif event.key == pygame.K_LEFT:
                    player_x_speed = -10
            elif event.type == pygame.KEYUP:
                    player_x_speed = 0
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_x = 400
                    player_y = 225
                    score = 0
                    gameover = False

    # 2) 배경화면 스크롤
    bgY += 10
    bgY2 += 10
    if bgY > 450:
        bgY = -450
    if bgY2 > 450:
        bgY2 = -450
    screen.blit(bg, (0, bgY))
    screen.blit(bg, (0, bgY2))

    # 3) Score 표시
    if gameover == False:
        score += 1
    score_text = font2.render("score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # 4) 물체 움직이기 (좌표 업데이트)
    player_x += player_x_speed
    player_y += player_y_speed

    for i in range(num_of_enemy):
        enemy_x[i] += enemy_x_speed[i]
        enemy_y[i] += enemy_y_speed[i]

    # 5) 벽에 부딪힘 처리
    if player_x > 780:
        player_x = 780
    if player_x < 0:
        player_x = 0

    for i in range(num_of_enemy):
        if enemy_x[i] > 800:
            enemy_x_speed[i] = -10
        if enemy_x[i] < 0:
            enemy_x_speed[i] = 10
        if enemy_y[i] > 450:
            enemy_y_speed[i] = -10
        if enemy_y[i] < 0:
            enemy_y_speed[i] = 10

    # 6) 비행체 그리기
    screen.blit(spaceship, (player_x, player_y))
    for i in range(num_of_enemy):
        screen.blit(enemy, (enemy_x[i], enemy_y[i]))

    # player update
    #player.update(screen, player_x_speed, player_y_speed)

    # 7) 물체 충돌 처리
    for i in range(num_of_enemy):
        if abs(player_x - enemy_x[i]) < 30 and abs(player_y - enemy_y[i]) < 30:
            soundObj.play() 
            gameover = True

    # 8) Game Over
    if gameover == True:
        screen.blit(explosion, (player_x-50, player_y-50))
        text = font1.render("Game Over", True, WHITE)
        screen.blit(text, (400 - text.get_width() // 2, 240 - text.get_height()))
        player_x_speed = 0
        player_y_speed = 0

    # 9) 실제 그림을 그리는 명령
    #pygame.display.flip()          # 전체 업데이트
    pygame.display.update()       # 부분 업데이트(rect 또는 rect_list)

# 게임 화면 종료
pygame.quit()

