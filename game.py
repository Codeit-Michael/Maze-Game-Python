import pygame

class Game:
	def __init__(self, maze, player, tile):
		self.maze = maze
		self.player = player
		self.tile = tile

	def is_collide(self, x, y):
		walls_collide_list = sum([cell.get_rects(self.tile) for cell in self.maze.grid_cells], [])
		tmp_rect = self.player.player_rect.move(x, y)
		if tmp_rect.collidelist(walls_collide_list) == -1:
			return False
		return True

	# game check
	def is_game_over(self):
		global time, score, record, FPS
		if time < 0:
			pygame.time.wait(700)
			player_rect.center = TILE // 2, TILE // 2
			set_record(record, score)
			record = get_record()
			time, score, FPS = 60, 0, 60


# player/game
# collision list
# timer, score, record
# pygame.time.set_timer(pygame.USEREVENT, 1000)
# time = 60
# score = 0
# record = get_record()
