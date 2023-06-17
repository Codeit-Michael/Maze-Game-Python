import pygame
from random import choice

class Cell:
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
		self.visited = False
		self.thickness = 3

	def draw(self, sc, tile):
		x, y = self.x * tile, self.y * tile
		if self.walls['top']:
			pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + tile, y), self.thickness)
		if self.walls['right']:
			pygame.draw.line(sc, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), self.thickness)
		if self.walls['bottom']:
			pygame.draw.line(sc, pygame.Color('darkorange'), (x + tile, y + tile), (x , y + tile), self.thickness)
		if self.walls['left']:
			pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + tile), (x, y), self.thickness)

	def get_rects(self, tile):
		rects = []
		x, y = self.x * tile, self.y * tile
		if self.walls['top']:
			rects.append(pygame.Rect( (x, y), (tile, self.thickness) ))
		if self.walls['right']:
			rects.append(pygame.Rect( (x + tile, y), (self.thickness, tile) ))
		if self.walls['bottom']:
			rects.append(pygame.Rect( (x, y + tile), (tile , self.thickness) ))
		if self.walls['left']:
			rects.append(pygame.Rect( (x, y), (self.thickness, tile) ))
		return rects

	def check_cell(self, x, y, cols, rows, grid_cells):
		find_index = lambda x, y: x + y * cols
		if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
			return False
		return grid_cells[find_index(x, y)]

	def check_neighbors(self, cols, rows, grid_cells):
		neighbors = []
		top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
		right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
		bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
		left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
		if top and not top.visited:
			neighbors.append(top)
		if right and not right.visited:
			neighbors.append(right)
		if bottom and not bottom.visited:
			neighbors.append(bottom)
		if left and not left.visited:
			neighbors.append(left)
		return choice(neighbors) if neighbors else False
