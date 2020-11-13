import pygame

class Scene(pygame.sprite.Sprite):
	def __init__(self, filename, width, height):
		pygame.sprite.Sprite.__init__(self)
		#self.screen_width = width
		#self.screen_height = height
		image = pygame.image.load(filename)
		self.bg_image = image.convert()
		self.screen_rect = image.get_rect()
		self.dialog = pygame.Surface((width, height/6))
		self.dialog.fill(pygame.Color(255,255,255))
		self.dialog_rect = pygame.rect(0, 0, width, height/6)

	def draw(self, surface):
		surface.blit(self.bg_image, self.screen_rect)
		surface.blit(self.dialog, self.dialog_rect)