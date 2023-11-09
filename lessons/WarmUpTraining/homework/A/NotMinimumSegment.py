class NotMinSlice:
	def __init__(self, mass):
		self.mass = mass

	def get(self,l,r):
		res = self.mass[l]
		for i in range(l+1, r+1):
			if res<self.mass[i]:
				return self.mass[i]
			elif res == self.mass[i]:
				continue
			else:
				return res
		return 'NOT FOUND'

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    mass = list(map(int, input().split()))
    go = NotMinSlice(mass)
    for i in range(M):
	    l, r = list(map(int, input().split()))
	    print(go.get(l, r))