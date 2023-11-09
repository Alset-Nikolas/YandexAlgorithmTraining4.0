def merger(mass1, mass2):
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



if __name__ == '__main__':
	n = input()
	mass1 = list(map(int, input().split()))
	m = input()
	mass2 = list(map(int, input().split()))
	result = merger(mass1, mass2)
	print(' '.join(str(x) for x in result))