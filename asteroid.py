from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position, radius, velocity)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)