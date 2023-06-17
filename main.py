"""
[/] 1. Access and Generate Maze
	[/] generate first before draw
[/] 2. Draw maze
[ ] 3. Add Player
[ ] 4. Create Controls
[ ] 5. Game functions
	[ ] Game state
	[ ] Message
		[ ]	add message draw from early game, if False don't draw, if True then draw
	[ ] clock
"""


import pygame
from maze import Maze

class Main():
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.game_over = False
		self.FPS = pygame.time.Clock()

	def _draw(self, maze, tile):
		[cell.draw(self.screen, tile) for cell in maze.grid_cells]
		pygame.display.flip()

	def main(self, frame_size, tile):
		self.screen.fill("white")
		cols, rows = frame_size[0] // tile, frame_size[-1] // tile
		maze = Maze(cols, rows)
		maze.generate_maze()
		while self.running:

			# if game.is_game_over(frame):
			# 	self.is_arranged = True
			# 	game.message(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				# if event.type == pygame.KEYDOWN:
				# 	if not self.is_arranged:
				# 		if game.arrow_key_clicked(event):
				# 			frame.handle_click(event)

			self._draw(maze, tile)
			self.FPS.tick(60)	
		pygame.quit()


if __name__ == "__main__":
	window_size = (602, 602)
	RES = (window_size[0] + 150, window_size[-1])
	tile = 20
	screen = pygame.display.set_mode(RES)
	pygame.display.set_caption("Slide Puzzle")

	game = Main(screen)
	game.main(window_size, tile)
