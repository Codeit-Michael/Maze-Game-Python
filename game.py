import pygame

pygame.font.init()

class Game:
	def __init__(self):
		self.font = pygame.font.SysFont("impact", 35)
		self.message_color = pygame.Color("darkorange")

	def add_goal_point(self, goal_cell, tile, screen):
		# adding gate for the goal point
		img_path = f'img/gate.png'
		img = pygame.image.load(img_path)
		img = pygame.transform.scale(img, (tile, tile))
		screen.blit(img, (goal_cell.x * tile, goal_cell.y * tile))

	def message(self):
		msg = self.font.render('You Win!!', True, self.message_color)
		return msg

	def is_game_over(self, player):
		if player.x >= 582 and player.y >= 582:
			return True