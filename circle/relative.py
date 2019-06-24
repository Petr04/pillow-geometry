def relative(center, coord):
	return ( (coord[0] - center[0]), (center[1] - coord[1]) )

def absolute(center, coord):
	return ( (coord[0] + center[0]), (center[1] - coord[1]) )
