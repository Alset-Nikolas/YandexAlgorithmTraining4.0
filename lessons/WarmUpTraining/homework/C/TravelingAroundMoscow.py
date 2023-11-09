import math


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.RR = self.x ** 2 + self.y ** 2
		self.R = self.RR ** 0.5
		self.pfi = self.__pfi()
		self.arc_X = self.R * self.pfi if self.x != 0 else math.pi / 2 * self.R
		self.arc_Y = 2 * math.pi * self.R / 4 - self.arc_X if self.x != 0 else 0

	def __pfi(self):
		if self.x == 0:
			return 0
		return round(math.atan(abs(self.y) / abs(self.x)), 6)

	def calc_arcs_by_angle(self, angle: float):
		if angle >= 0:
			return round(self.R * angle, 6)
		return  round(self.pfi/2 - self.R * angle, 6)

class CalcRout:
	def __init__(self, p1: Point, p2: Point):
		if p1.R > p2.R:
			p1, p2 = p2, p1
		self.p1 = p1
		self.p2 = p2

	def get_vars(self):
		if self.p1.x * self.p2.x >= 0 and self.p1.y * self.p2.y >= 0:
			return 1
		if sum(
				[
					bool(self.p1.x * self.p2.x >= 0),
					bool(self.p1.y * self.p2.y >= 0)
				]
		) == 1:
			return 2
		return 3

	def calc(self):
		flag = self.get_vars()
		L_X_1, L_Y_1 = self.p1.arc_X, self.p1.arc_Y
		L_X_2, L_Y_2 = self.p2.arc_X, self.p2.arc_Y
		if flag == 1:
			return min(L_X_1 + L_X_2, L_Y_1 + L_Y_2) + (self.p2.R - self.p1.R)
		if flag == 2:
			if self.p1.x * self.p2.x >= 0:
				return L_X_1+L_X_2 + (self.p2.R - self.p1.R)
			return  L_Y_1+L_Y_2+ (self.p2.R - self.p1.R)
		return self.p1.R + self.p2.R
	def answer(self):
		res = self.calc()
		return min(res, self.p1.R + self.p2.R)
if __name__ == '__main__':
	x1, y1, x2, y2 = list(map(int, input().split()))
	p1, p2 = Point(x1, y1), Point(x2, y2)
	print(p1.R, p2.R)
	rout = CalcRout(p1, p2)
	print(rout.answer())


	# assert (get_min_dist(444444, 333333, 888888, 666666)
	#         == approx(555555.0, abs=1e-6))  # test # 8
