import sys
import pygame


def run_game():
    # 进行初始化屏幕
    pygame.init()
    # 设置了屏幕大小和游戏标题
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # 设置背景颜色
    bg_color = (230,230,230)
    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#         每次循环重绘屏幕
        screen.fill(bg_color)
#         让绘制的屏幕可见
        pygame.display.flip()

run_game()

