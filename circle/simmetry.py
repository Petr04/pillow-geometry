def simmetry(coord):
	ret = []
	ret.append(tuple(coord))

	coord_rev = list(coord)
	coord_rev.reverse()
	coord_rev[0] *= -1
	ret.append(tuple(coord_rev))

	ret_new = []
	for i in ret:
		ret_new.append(tuple([n * -1 for n in i]))

	return tuple(ret + ret_new)

if __name__ == '__main__':
	l = list(map(int, input().split()))
	print(simmetry(l))
