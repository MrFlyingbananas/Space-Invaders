import pygame
import os
class Bunker(pygame.sprite.Sprite):
	WIDTH = 65
	def __init__(self, pos, *groups):
		pygame.sprite.Sprite.__init__(self, groups)
		print(os.path.join('Assets'))
		self.image = pygame.image.load(os.path.join('Assets', 'bunker.png'))
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def update():
		pass

	
