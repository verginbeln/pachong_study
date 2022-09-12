import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()       # 1初始化操作
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200,800))    # 2创建游戏窗口
    pygame.display.set_caption('我的游戏')# 设置游戏名
    ship = Ship(ai_settings, screen)   #创建一艘飞船
    bullets = Group()             #引入子弹编组
    alien = Alien(ai_settings, screen)
    aliens = Group()              #引入外星人编组

    #创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # 让游戏保持一直运行的状态
    # game loop 游戏循环（检测事件）
    while True:
       gf.check_events(ai_settings, screen, ship, bullets)       #响应按键和鼠标事件
       ship.update()
       gf.update_bullets(ai_settings,screen, ship, aliens, bullets)
       gf.update_aliens(ai_settings, ship, aliens)
       gf.update_screen(ai_settings, screen, ship, alien, aliens, bullets)  ##更新屏幕上的图像，并切换到新屏幕


if __name__ == '__main__':
    run_game()

