import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        splitted_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        splitted_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        trajectory_angle = random.uniform(20, 50)
        splitted_asteroid_1.velocity = self.velocity.rotate(trajectory_angle) * 1.2
        splitted_asteroid_2.velocity = self.velocity.rotate(-trajectory_angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt