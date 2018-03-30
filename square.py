#!/usr/bin/python

class Square:
	''' A square in a sliding puzzle game '''
	color = ''
	label = ''
	position = (-1,-1)
	dim = (0,0)
	height = 0
	visible = True
	winning_position = (0,0)
	def __init__(self, x, y, label, w, h, color, font):
		self.position = (x,y)
		self.winning_position = (x,y)
		self.dim = (w,h)
		self.color = color
		self.font = font
		self.label = label
	
	def check_proximity(self, xy):
		''' take a x/y position (as a tuple) and see if it is next to the current position '''
		if self.position == (-1,-1): return False
		if self.position == xy: return False
		if (abs(xy[0] - self.position[0]) <= 1 and xy[1] == self.position[1]) or (abs(xy[1] - self.position[1]) <= 1 and xy[0] == self.position[0]):
			return True
		return False
		
	def draw_square(self, draw, screen):
		''' add the square to the draw object and blit it to the screen'''
		if self.visible:
			(x1,y1) = self.position
			(w,h) = self.dim
			(x,y) = (x1 * w,y1 * h)
			draw.rect(screen, self.color, (x,y,w,h))
			f = self.font.render(self.label,True,(0,0,0))
			(fwidth,fheight) = self.font.size(self.label)
			#center the font
			(fx,fy) = (x + (w - fwidth)/2,y + (h - fheight)/2)
			screen.blit(f,(fx,fy))
		return draw

	def square_locater(self, pos):
		(x1, y1) = self.position
		(w, h) = self.dim
		(x, y) = (x1 * w, y1 * h)
		if pos[0] >= x and pos[1] >= y and pos[0] <= x + w and pos[1]<= y+h:
			return True
		else:
			return False

	def right_spot(self):
		if self.position == self.winning_position:
			return True
		else:
			return False

