import pygame
###################################################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init()   # 초기화 (반드시 필요. pygame을 호출하면 반드시 init-초기화)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름
# pygame에서는 event roop가 항상 진행되고 있어야 창이 꺼지지 않음

# FPS
clock = pygame.time.Clock()
###################################################################################
# 여기까지 무조건 해야 하는 부분


# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 이벤트 루프 - 반드시 설정
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의의
    # 화면 밖으로 벗어나지 않도록 가로, 세로 경계값 처리

    # 4. 이미지 간 충돌 처리

    # 5. 화면에 그리기
    pygame.display.update() # 게임 화면을 다시 그리기. 반드시 계속 호출해줘야 변경사항 반영

# pygame 종료
pygame.quit()

