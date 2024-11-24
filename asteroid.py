from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position, radius, velocity)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):        
        pygame.sprite.Sprite.kill(self)       
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            left_vector = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            right_vector = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(self.position, new_radius, left_vector)
            right_asteroid = Asteroid(self.position, new_radius, right_vector)