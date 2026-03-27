import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot (CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        pass
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        pass
    def update(self, dt):
        self.position += self.velocity * dt
        pass
