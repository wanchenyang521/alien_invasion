import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group

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
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting,screen,ship,bullets)
        # 相应事件
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting,screen,ship,bullets)

run_game()

