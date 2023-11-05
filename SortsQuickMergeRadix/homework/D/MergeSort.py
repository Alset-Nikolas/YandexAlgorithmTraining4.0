def merge(mass1, mass2):
	mass3 = [0] * (len(mass2) + len(mass1))
	k = 0
	i, j = 0,0
	while i< len(mass1) and j< len(mass2):
		if mass1[i]<= mass2[j]:
			mass3[k] = mass1[i]
			i += 1
		else:
			mass3[k] = mass2[j]
			j += 1
		k += 1
	for l, mass in [ (i,mass1), (j,mass2)]:
		while l < len(mass):
			mass3[k] = mass[l]
			l += 1
			k += 1
	return mass3



def merge_sort(mass,l, r):
	if l >= r or r - l <= 1:
		return mass[l:r]
	m = (r+l)//2
	mass1 = merge_sort(mass, l, m)
	mass2 = merge_sort(mass, m, r)
	return merge(mass1, mass2)

if __name__ == '__main__':
    n = int(input())
    mass =list(map(int, input().split()))
    mass = merge_sort(mass, 0, len(mass))
    print(' '.join(str(x) for x in mass))