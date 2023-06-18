import pygame

pygame.font.init()

class Game:
	def __init__(self):
		self.font = pygame.font.SysFont("impact", 35)
		self.background_color = pygame.Color("darkslategray")
		self.message_color = pygame.Color("darkorange")

	def add_goal_point(self, goal_cell, screen):
		# adding gate for the goal point
		goal_cell.walls["right"] = False
		img_path = f'img/gate.png'
		img = pygame.image.load(img_path)
		img = pygame.transform.scale(img, (30, 30))
		screen.blit(img, (goal_cell.x * 30, goal_cell.y * 30))

	def message(self, screen):
		screen.fill(self.background_color, (5, 460, 440, 35))
		instructions = self.font.render('You Win!!', True, self.message_color)
		screen.blit(instructions,(125,460))

	def is_game_over(self, player):
		if player.x >= 582 and player.y >= 582:
			return True