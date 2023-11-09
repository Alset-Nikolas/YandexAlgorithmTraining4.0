def add_two_fractions(x1, y1, x2, y2):
	m = x1*y2 + x2*y1
	n = y1*y2
	mass = list(range(m+1))
	for i in range(2, m+1, 1):
		if mass[i] is None:
			continue
		j = 2
		while i*j <= m:
			mass[i*j] = None
			j += 1
		while m % mass[i] == 0 and n % mass[i] == 0:
			m //= mass[i]
			n //= mass[i]
		if mass[i] == m or mass[i] == n or mass[i] >=m or mass[i] >= n:
			break
	return m, n



if __name__ == '__main__':
	x1, y1, x2, y2 = list(map(int, input().split()))
	m,n =add_two_fractions(x1, y1, x2, y2)
	print(m, n)