import pygame

pygame.font.init()

class Game:
	def __init__(self):
		self.font = pygame.font.SysFont("impact", 35)
		self.background_color = pygame.Color("darkslategray")
		self.message_color = pygame.Color("darkorange")

	def message(self, screen):
		screen.fill(self.background_color, (5, 460, 440, 35))
		instructions = self.font.render('You Win!!', True, self.message_color)
		screen.blit(instructions,(125,460))

	def is_game_over(self, player, screen):
		if player.x >= 582 and player.y >= 582:
			self.message(screen)
			return True