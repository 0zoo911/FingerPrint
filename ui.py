import pygame
import pygame_gui
import time
import sys
from pygame.locals import *
from btn import Button

pygame.init()

# 화면 크기 설정
WIDTH = 900
HEIGHT = 550

s_width = 400
s_height = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("지문 등록")

# UI 매니저 생성
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# 등록 버튼 생성
R_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((125, 205), (200, 150)),
                                      text='Registration',
                                      manager=manager)

# 최근 버튼 생성
W_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((355, 205), (200, 150)),
                                      text='Work',
                                      manager=manager)

# 퇴근 버튼 생성
L_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((585, 205), (200, 150)),
                                      text='Leave',
                                      manager=manager)
# 색상
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)
RED = (255,0,0)

# 폰트 설정
font = pygame.font.Font(None, 36)

def new_form():
    s_width = 400
    s_height = 300
    
    form = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption("PassWord")
    
    # 새 창에 메시지 출력
    form.fill((255, 255, 255))
    message = font.render("Hello, World!", True, (0, 0, 0))
    message_rect = message.get_rect(center=(s_width // 2, s_height // 2))
    form.blit(message, message_rect)

    return form

clock = pygame.time.Clock()
done = True
while done:
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = False
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == R_button:
                form = new_form()
                # form = pygame.display.set_mode((s_width, s_height))
                # pygame.display.set_caption("PassWord")
                
                
        # UI 매니저에 이벤트 전달
        manager.process_events(event)

    # 배경색 설정
    screen.fill((WHITE))
    
     # UI 매니저 업데이트
    manager.update(time_delta)

    # UI 매니저를 통해 UI 요소 그리기
    manager.draw_ui(screen)

    if 'form' in locals():
        form.blit(form, (WIDTH // 2 - s_width // 2, HEIGHT // 2 - s_height // 2))

    pygame.display.update()
    
pygame.quit()
