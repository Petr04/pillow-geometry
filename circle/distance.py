from math import sqrt

def distance(a, b):
	s = 0
	for a_zip, b_zip in zip(a, b):
		s += abs(a_zip - b_zip) ** 2

	return sqrt(s)

if __name__ == '__main__':
	print(distance(*[list(map(int, input().split())) for _ in range(2)]))
