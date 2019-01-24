import sys
import pygame


def check_events():
    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings,screen,ship):
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让绘制的屏幕可见
    pygame.display.flip()
