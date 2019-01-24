import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
def run_game():
    # 进行初始化屏幕
    pygame.init()
    # 创建设置对象
    ai_setting = Setting()
    # 设置了屏幕大小和游戏标题
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船对象
    ship = Ship(ai_setting,screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 相应事件
        ship.update()
        gf.update_screen(ai_setting,screen,ship)

run_game()

