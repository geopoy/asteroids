import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            nv = random.uniform(20, 50)
            as1 = self.velocity.rotate(nv)
            as2 = self.velocity.rotate(-nv)
            nr = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, radius=(self.radius-ASTEROID_MIN_RADIUS))
            new_asteroid2 = Asteroid(self.position.x, self.position.y, radius=(self.radius-ASTEROID_MIN_RADIUS))
            new_asteroid.velocity = as1 * 1.2
            new_asteroid2.velocity = as2 * 1.2
