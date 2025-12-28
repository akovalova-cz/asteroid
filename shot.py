import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt