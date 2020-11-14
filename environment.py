import random
import pygame
import quizdata

class Scene(pygame.sprite.Sprite):
	def __init__(self, filename, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.screen_width = width
		self.screen_height = height
		image = pygame.image.load(filename)
		self.bg_image = image.convert()
		self.screen_rect = image.get_rect()
		self.dialog = pygame.Surface((width, height/6))
		self.dialog.fill(pygame.Color(255,255,255))
		self.dialog_rect = pygame.Rect(0, height - height/6, width, height)
		sysfont = pygame.font.get_default_font()
		self.font_obj = pygame.font.SysFont(sysfont, 35)

	def draw(self, surface):
		surface.blit(self.bg_image, self.screen_rect)
		surface.blit(self.dialog, self.dialog_rect)



#--------------------------------------------------------------#
class ShopScene(Scene):
	def __init__(self, width, height):
		Scene.__init__(self, "Images/shop.jpg", width, height)
		self.quiz_bank = quizdata.QuizData()
		self.phase = 0
		self.my_question = ""
		self.my_answer = ""
		self.all_answers = ""
		self.bottom_dialog = pygame.Rect(0, height - height/12, width, height)

	def updateDisplayLogic(self, answer = ""):
		self.phase += 1
		self.getQuestions()
		return self.my_answer == answer

	def getQuestions(self):
		self.my_question = ""
		self.my_answer = ""
		self.all_answers = ""
		if self.phase == 1:
			self.my_question = random.choice(list(self.quiz_bank.English.keys()))
			self.my_answer = self.quiz_bank.English[self.my_question][0]
			self.all_answers = self.quiz_bank.English[self.my_question][1]
		elif self.phase == 3:
			self.my_question = random.choice(list(self.quiz_bank.Geography.keys()))
			self.my_answer = self.quiz_bank.Geography[self.my_question][0]
			self.all_answers = self.quiz_bank.Geography[self.my_question][1]

	def draw(self, surface):
		Scene.draw(self, surface)

		if self.phase == 0:
			mytext = "Welcome to the Shop. Let us test your Knowledge"
			
			text_surface = self.font_obj.render(mytext, False, pygame.Color(0,0,0))
			surface.blit(text_surface, self.dialog_rect)
		else:
			top_text_surface = self.font_obj.render(self.my_question, True, pygame.Color(0,0,0))
			bottom_text_surface = self.font_obj.render(self.all_answers, True, pygame.Color(0,0,0))
			surface.blit(top_text_surface, self.dialog_rect)
			surface.blit(bottom_text_surface, self.bottom_dialog)
			





#--------------------------------------------------------------#
class ActionScene(Scene):
	def __init__(self, width, height):
		Scene.__init__(self, "Images/bg.jpg", width, height)

	def draw(self, surface, health, ammo):
		Scene.draw(self, surface)


#if __name__ == '__main__':
#	data = quizdata.QuizData()
#	print(data.English)