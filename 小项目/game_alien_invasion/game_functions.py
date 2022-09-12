import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        print("右键按下")
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        print("左键按下")
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        print("空格按下")
        # 创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:  #限制子弹个数
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_1:   #快捷键q退游
        sys.exit()
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        print("右键松了")
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        print("左键松了")
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        print("空格松了")


def check_events(ai_settings, screen, ship, bullets):
# """响应按键和鼠标事件"""
# 4.检测事件（比如鼠标，键盘的点击检测）
# 固定写法，event，get可以一次获取多个事件，所以要循环遍历.监视键盘和鼠标事件
# 每当用户按键时，都将在Pygame中注册一个事件。事件都是通过方法pygame.event.get()获取的，
    for event in pygame.event.get():
        # 判断是否退出（点×）
        if event.type == pygame.QUIT:
            # 退出函数（一般不会这么简单，要保存）
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #每次按键都被注册为一个KEYDOWN事件。
            check_keydown_events(event, ai_settings, screen, ship, bullets )
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, aliens, bullets):
        screen.fill(ai_settings.bg_color)
        # 在飞船和外星人后面重绘所有子弹
        for bullet in bullets.sprites():  #方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵
            bullet.draw_bullet()
        ship.blitme()                      #确保它出现在背景前面
        # alien.blitme()
        aliens.draw(screen)              #编组画出来里面
        # bg_color = (255,182,193)
        # screen.fill(bg_color)
        # screen.fill((255,182,193))
        # 或者screen.fill(pygame.Color(255,182,193))   # 设置背景颜色,元组 0-255
        pygame.display.flip()  # 让最近绘制的屏幕可见
def update_bullets(ai_settings,screen, ship, aliens, bullets):
       bullets.update()                ## 更新子弹的位置
       for bullet in bullets.copy():   #在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
           if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
       #print(len(bullets))
       # 检查是否有子弹击中了外星人
       # 如果是这样，就删除相应的子弹和外星人
       collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
       if len(aliens) == 0:
           bullets.empty()
           create_fleet(ai_settings, screen, aliens, ship)
def create_fleet(ai_settings, screen, aliens, ship):
    #创建外星人群
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_aliens_y = get_number_aliens_y(ai_settings, alien_height, ship_height)
    for row_number in range(number_aliens_y):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            alien = Alien(ai_settings, screen)
            alien.x = 0 + alien_width * alien_number
            alien.y = 0 + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)
def get_number_aliens_x(ai_settings, alien_width):
    # available_space_x = ai_settings.screen_width - 2 *alien_width
    # number_aliens_x = int(available_space_x / (2 * alien_width))
    number_aliens_x = int((ai_settings.screen_width) / alien_width)
    return number_aliens_x
def get_number_aliens_y(ai_settings, alien_height, ship_height):
    number_aliens_y = int((ai_settings.screen_height - 6*alien_height - ship_height)/alien_height)
    return number_aliens_y
def check_fleet_edges(ai_settings, aliens):
     # """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
# """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, ship, aliens):
# 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  ## 更新位置
# 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")