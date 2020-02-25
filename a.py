import pygame

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

hero = pygame.sprite.Group()
blocks = pygame.sprite.Group()


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(hero)
        self.x, self.y = x, y
        self.image = pygame.Surface([20, 20])
        pygame.draw.rect(self.image, (0, 0, 255), (0, 0, 20, 20), 0)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y


class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(hero)
        self.x, self.y = x, y
        self.image = pygame.Surface([50, 10])
        pygame.draw.rect(self.image, (128, 128, 128), (0, 0, 50, 10), 0)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y


check = False
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if event.button == 3:
                check = True
                Hero(x, y)
            if event.button == 1:
                Blocks(x, y)
    blocks.draw(screen)
    hero.draw(screen)
    clock.tick(200)
    pygame.display.flip()
pygame.quit()
