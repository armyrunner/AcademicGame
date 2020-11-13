import pygame

class Scene(width, height):
	"""docstring for Scene"""
	def __init__(self, width, height, bg_color):
		pygame.display.init()
		self.window = pygame.display.set_mode(size(width, height))
		self.window.fill(fill_color = pygame.Color(r, g, b))