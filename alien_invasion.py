import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from alien import Alien
from scoreboard import Scoreboard
def run_game():
    # 进行初始化屏幕
    pygame.init()
    # 创建设置对象
    ai_settings = Setting()
    # 设置了屏幕大小和游戏标题
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船对象
    ship = Ship(ai_settings,screen)
    # # 创建一个外星人
    # alien = Alien(ai_settings,screen)
    # 创建一个用于编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建按钮
    play_button = Button(ai_settings,screen,"Play")
    # 创建统计信息实例，并创建记分牌
    sb = Scoreboard(ai_settings,screen,stats)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            # 相应事件
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()

