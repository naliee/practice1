import pygame

pygame.init()   # 초기화 (반드시 필요. pygame을 호출하면 반드시 init-초기화)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Lina Game") # 게임 이름
# pygame에서는 event roop가 항상 진행되고 있어야 창이 꺼지지 않음

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\이벌브소프트\\Desktop\\PythonWorkspace\\pygame.basic\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\이벌브소프트\\Desktop\\PythonWorkspace\\pygame.basic\\character.png")
character_size = character.get_rect().size  # 이미지 크기 구해 옴
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도 - 이동 키 눌렀을 때 이동하는 정도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    # 캐릭터가 1초 동안 100만큼 이동을 해야 함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼!
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 몇 만큼 이동? 5만큼! <= 이동 속도!

    dt = clock.tick(30) # 게임 화면의 초당 프레임 수를 설정. 작아질수록 뚝뚝 끊기는 느낌

    # event: 사용자가 이벤트(키보드, 마우스 움직임)을 만들고있는지
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창을 끄는 X버튼을 눌러 껐을 경우 (창이 닫히는 이벤트 발생)
            running = False

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인인
           if event.key == pygame.K_LEFT:
                to_x -= character_speed
           elif event.key == pygame.K_RIGHT:
                to_x += character_speed
           elif event.key == pygame.K_UP:
                to_y -= character_speed
           elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 화면 밖으로 벗어나지 않도록 조정 - 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 화면 밖으로 벗어나지 않도록 조정 - 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기. 맨 왼쪽, 맨 위가 0,0

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update() # 게임 화면을 다시 그리기. 반드시 계속 호출해줘야 변경사항 반영

# pygame 종료
pygame.quit()

