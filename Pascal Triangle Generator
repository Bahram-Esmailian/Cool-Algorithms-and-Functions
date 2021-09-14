#Simple Pascal Triangle Generator created and written by Bahram Esmailian

def PascalTriangle(n):
	if n == 1:
		return [[1]]
	elif n == 2:
		return [[1],[1,1]]
	elif n > 2:
		triangle = PascalTriangle(n-1)
		triangle = triangle + [[1] + [triangle[n-2][i] + triangle[n-2][i+1] for i in range(len(triangle[n-2])-1)] + [1]]
		return triangle

#prints the Pascal triangle up to the n'th level
print(PascalTriangle(n))
