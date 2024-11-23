import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	actor = Player(x, y, PLAYER_RADIUS)
	field = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill('black')
		dt = clock.tick(60)/1000
		for thing in updatable:
			thing.update(dt)
		for thing in drawable:
			thing.draw(screen)		
		pygame.display.flip()

if __name__ == "__main__":
	main()
