
import pygame
import random

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def collision(self):
        self.velocity[0] = -self.velocity[0]
        if(self.velocity[0] > 0):
            self.velocity[0] += 1.0
        else:
            self.velocity[0] -= 1.0