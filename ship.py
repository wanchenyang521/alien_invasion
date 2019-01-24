import pygame

class Ship():

    # 初始化飞船
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.settings = ai_settings
        # 加载图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 飞船移动的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False
        # 飞船属性center储存小数
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.bottom -= self.settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom