import pygame
from random import uniform
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = uniform(20, 50)
        rotated_velocity1 = self.velocity.rotate(angle)
        rotated_velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius / 2
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = rotated_velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = rotated_velocity2