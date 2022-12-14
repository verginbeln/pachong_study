import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings   #那里面的速度条件
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # """根据移动标志调整飞船的位置"""
        # if self.moving_right:
        #     self.rect.centerx += 1    # 向右移动飞船
        # elif self.moving_left:           #rect的centerx等属性只能存储整数值
        #     self.rect.centerx -= 1    # 向zuo移动飞船   只能整数,要小数,因为越来越快
        if self.moving_right and self.rect.right < self.screen_rect.right:  #限制飞船的活动范围
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        # print(self.center)
        # print(self.rect.centerx)
        self.rect.centerx = self.center  #self.rect.centerx将只存储self.center的整数部分，但对显示飞船而言，这问题不大
        # print(self.rect.centerx)
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)   #blit 停留