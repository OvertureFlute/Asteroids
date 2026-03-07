from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        asteroid1 = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2
        asteroid2.velocity = self.velocity.rotate(-1 * random.uniform(20, 50)) * 1.2