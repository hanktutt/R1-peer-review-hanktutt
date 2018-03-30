#!/usr/bin/env python
import sys, pygame, random
from square import Square
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (600,600)
dimensions = (rows,columns) = (4,4)
FPS = 60
black = (0,0,0)
#colors taken from https://yeun.github.io/open-color/
colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]	

def calculate_xy(pos,puzzle):
	''' calculates which square is the target '''
	w = width / columns
	h = height / rows
	to_return = (int(pos[0]//w),int(pos[1]//h))
	return to_return

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("arial",64)
	clock = pygame.time.Clock()
	winning = False
	puzzle = []
	(w,h) = (screen_size[0]/columns,screen_size[1]/rows)
	for i in range(rows):
		for j in range(columns):
			position = j*rows + i
			color = colors[position]
			puzzle.append(Square(i,j,str(position+1),w,h,color,font))
	puzzle[15].visible=False
	magic_block = puzzle[15]

	how_randomized = 3  # how much we want to randomize the puzzle
	randomize_probability = 90  # 20% of switching with the magic square
	for h in range(how_randomized):
		for p in puzzle:
			if p.check_proximity(magic_block.position) and random.randrange(100) < randomize_probability:
				temp = p.position
				p.position = magic_block.position
				magic_block.position = temp

	while True:
		clock.tick(FPS)

		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONUP and not winning:
				pos = pygame.mouse.get_pos()
				for p in puzzle:
					if p.square_locater(pos) == True:
						if p.check_proximity(magic_block.position):
							new_spot= p.position
							p.position=magic_block.position
							magic_block.position= new_spot
				winning = True
				for p in puzzle:
					if not p.right_spot():
						winning = False
				if winning:
					magic_block.visible = True
					print("You Won!")


		for p in puzzle:
			p.draw_square(pygame.draw,screen)		

		
		pygame.display.flip()

if __name__ == '__main__':
	main()