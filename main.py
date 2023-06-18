"""
[/] 1. Access and Generate Maze
	[/] generate first before draw
[/] 2. Draw maze
[/] 3. Add Player
[/] 4. Create Controls
[ ] 5. Game functions
		[/] Game state
		[/] Message
			[ ]	add message draw from early game, if False don't draw, if True then draw
		[ ] clock
"""


import pygame
from maze import Maze
from player import Player
from game import Game

pygame.init()

class Main():
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.game_over = False
		self.FPS = pygame.time.Clock()

	def _draw(self, maze, tile, player, game):
		[cell.draw(self.screen, tile) for cell in maze.grid_cells]
		player.draw(self.screen)
		game.message(self.screen) if self.game_over else False
		game.add_goal_point(maze.grid_cells[-1], self.screen)
		player.update()
		pygame.display.flip()

	def main(self, frame_size, tile):
		cols, rows = frame_size[0] // tile, frame_size[-1] // tile
		maze = Maze(cols, rows)
		game = Game()
		starting_pos = maze.grid_cells[0]
		player = Player(tile // 3, tile // 3)

		maze.generate_maze()
		while self.running:
			self.screen.fill("white")

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			if event.type == pygame.KEYDOWN:
				if not self.game_over:
					if event.key == pygame.K_LEFT:
						player.left_pressed = True
					if event.key == pygame.K_RIGHT:
						player.right_pressed = True
					if event.key == pygame.K_UP:
						player.up_pressed = True
					if event.key == pygame.K_DOWN:
						player.down_pressed = True
					player.check_move(tile, maze.grid_cells, maze.thickness)
		
			if event.type == pygame.KEYUP:
				if not self.game_over:
					if event.key == pygame.K_LEFT:
						player.left_pressed = False
					if event.key == pygame.K_RIGHT:
						player.right_pressed = False
					if event.key == pygame.K_UP:
						player.up_pressed = False
					if event.key == pygame.K_DOWN:
						player.down_pressed = False
					player.check_move(tile, maze.grid_cells, maze.thickness)

			if game.is_game_over(player):
				self.game_over = True
				player.left_pressed = False
				player.right_pressed = True
				player.up_pressed = False
				player.down_pressed = False

			self._draw(maze, tile, player, game)
			self.FPS.tick(60)	
		pygame.quit()


if __name__ == "__main__":
	window_size = (602, 602)
	RES = (window_size[0] + 150, window_size[-1])
	tile = 30
	screen = pygame.display.set_mode(RES)
	pygame.display.set_caption("Maze")

	game = Main(screen)
	game.main(window_size, tile)
