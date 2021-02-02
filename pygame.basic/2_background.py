import pygame

pygame.init()   # 초기화 (반드시 필요. pygame을 호출하면 반드시 init-초기화)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Lina Game") # 게임 이름
# pygame에서는 event roop가 항상 진행되고 있어야 창이 꺼지지 않음

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\이벌브소프트\\Desktop\\PythonWorkspace\\pygame.basic\\background.png")


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    # event: 사용자가 이벤트(키보드, 마우스 움직임)을 만들고있는지
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창을 끄는 X버튼을 눌러 껐을 경우 (창이 닫히는 이벤트 발생)
            running = False

    # screen.fill((0, 0, 255))   # 이미지가 아닌 색으로 배경 채우기기
    screen.blit(background, (0, 0)) # 배경 그리기. 맨 왼쪽, 맨 위가 0,0

    pygame.display.update() # 게임 화면을 다시 그리기. 반드시 계속 호출해줘야 변경사항 반영

# pygame 종료
pygame.quit()

