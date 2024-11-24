import pygame
import sys
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
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
		for thing in asteroids:
			for thing2 in shots:
				if thing2.collision(thing):
					pygame.sprite.Sprite.kill(thing)
					pygame.sprite.Sprite.kill(thing2)
			if thing.collision(actor):
				print("Game Over!")
				sys.exit()
		for thing in drawable:
			thing.draw(screen)		
		pygame.display.flip()

if __name__ == "__main__":
	main()
