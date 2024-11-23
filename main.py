import constants 
import pygame
import player

def main():
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()
	x = constants.SCREEN_WIDTH/2
	y = constants.SCREEN_HEIGHT/2
	actor = player.Player(x, y, constants.PLAYER_RADIUS)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill('black')
		actor.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
