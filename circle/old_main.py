from PIL import Image, ImageDraw
from math import sqrt

from distance import distance

def next_coords(coord):
	return ( (coord[0]-1, coord[1]-1), (coord[0], coord[1]-1) )

def circle(draw, center, radius, color=tuple([0])*3):
	coord = ( center[0]+radius, center[1] )
	while True:
		draw.point(coord, color)
		print(coord)

		my_next_coords = next_coords(coord)
		print(my_next_coords)
		min_dist = distance(center, my_next_coords[0])
		coord = my_next_coords[0]
		for i in my_next_coords[1:]:
			new_dist = distance(center, i)
			if new_dist < min_dist:
				min_dist = new_dist
				coord = i

		print(coord)

		if coord[0] - center[0] < center[1] - coord[1]:
			break

image = Image.new('RGB', (100, 100), tuple([255])*3)
draw = ImageDraw.Draw(image)

draw.point((50, 50), (255, 0, 0))
circle(draw, (50, 50), 10, (255, 0, 0))
image.show()
