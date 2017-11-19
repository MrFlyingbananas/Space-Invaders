import pygame
from Bunker import Bunker


SCREEN_FILL = (60,0,0)
WIDTH = 800
HEIGHT = 600

def get_image(path):
	current_path = os.path.dirname(__file__)
	image_path = os.path.join(current_path, 'Assets')
	return pygame.image.load(os.path.join(image_path, path))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screenfill = SCREEN_FILL
quit = False
renderables = pygame.sprite.Group()
bunkers = [Bunker([((WIDTH-175)/4)*i - Bunker.WIDTH/2, 450], renderables) for i in range(1,5)]
def draw():
	renderables.draw(screen)

while not quit:
	events = []
	pressed_keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
		else: events.append(event)
	screen.fill(SCREEN_FILL)

	draw()
	#update

	
	pygame.display.flip()
	clock.tick(12)
pygame.quit()