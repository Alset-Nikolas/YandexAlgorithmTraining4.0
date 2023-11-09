def pprint(buckets, i):
	print('**********')
	print(f'Phase {i}')
	for i in range(len(buckets)):
		items = ', '.join(str(x) for  x in buckets[i]) if len(buckets[i])>0 else 'empty'
		print(f'Bucket {i}: {items}')

def init_buckets(mass):
	buckets = [[] for x in range(10)]
	for x in mass:
		x_ = x[-1]
		buckets[int(x_)].append(x)
	pprint(buckets, 1)
	return buckets
def radius_sort(mass):
	x0 = mass[0]
	print('Initial array:')
	print(', '.join(str(x) for x in mass))
	buckets = init_buckets(mass)

	phase = 2
	for j in range(len(x0)-2, -1,- 1):
		update_buckets = [[] for x in range(10)]
		for i in range(len(buckets)):
			for x in buckets[i]:
				x_ = x[j]
				update_buckets[int(x_)].append(x)
		buckets = update_buckets
		pprint(buckets, phase)
		phase += 1
	print('**********')
	print('Sorted array:')
	ans = []
	for i in range(len(buckets)):
		for x in buckets[i]:
			ans.append(x)
	print(', '.join(ans))



if __name__ == '__main__':
	n = int(input())
	mass = []
	for i in range(n):
		mass.append(input())
	ans = radius_sort(mass)

