from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position, radius, velocity)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt