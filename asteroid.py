import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()

        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(angle)
        second_velocity = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x = self.position.x
        y = self.position.y
    
        first_asteroid = Asteroid(x, y, new_radius)
        second_asteroid = Asteroid(x, y, new_radius)

        first_asteroid.velocity = first_velocity * 1.2
        second_asteroid.velocity = second_velocity * 1.2
