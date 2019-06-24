from PIL import Image, ImageDraw
from math import sqrt

from distance import distance
from simmetry import simmetry
from relative import relative, absolute

def next_coords(coord):
	return ( (coord[0]-1, coord[1]-1), (coord[0], coord[1]-1) )

def circle(draw, center, radius, color=tuple([0])*3):
	coord = ( center[0]+radius, center[1] )
	while True:
		simm = simmetry(relative(center, coord))
		for i in simm:
			draw.point(absolute(center, i), color)
			draw.point(absolute(center, (i[0], -i[1])), color)

		my_next_coords = next_coords(coord)

		min_dist = abs(radius - distance(center, my_next_coords[0]))
		coord = my_next_coords[0]

		for i in my_next_coords[1:]:
			new_dist = abs(radius - distance(center, i))
			if new_dist < min_dist:
				min_dist = new_dist
				coord = i

		if coord[0] - center[0] < center[1] - coord[1]:
			break

image = Image.new('RGB', (500, 500), tuple([255])*3)
draw = ImageDraw.Draw(image)

center = (200, 200)
color = (255, 0, 0)
radius = 100

draw.point(center, color)
circle(draw, center, radius, color)
image.show()
