import pygame
class Star():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def blitme(self):
        self.screen.blit(self.image, self.rect)