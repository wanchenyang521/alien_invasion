import sys
import pygame
from setting import Setting
from ship import Ship
def run_game():
    # 进行初始化屏幕
    pygame.init()
    # 创建设置对象
    ai_setting = Setting()
    # 设置了屏幕大小和游戏标题
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船对象
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#         每次循环重绘屏幕
        screen.fill(ai_setting.bg_color)
        ship.blitme()
#         让绘制的屏幕可见
        pygame.display.flip()

run_game()

