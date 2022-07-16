#A Bernoulli Number Generator created and written by Bahram Esmailian

import numpy as np
from fractions import Fraction
import sys

#This is higher than the base Python recursion limit, increase when needed
sys.setrecursionlimit(20000)

#generates a Pascal Triangle from which the Bernoulli number be generated
def PascalTriangle(n):
	if n == 1:
		return [[Fraction(1)]]
	elif n == 2:
		return [[Fraction(1)],[Fraction(1),Fraction(1)]]
	elif n > 2:
		triangle = PascalTriangle(n-1)
		triangle = triangle + [[Fraction(1)] + [triangle[n-2][i] + triangle[n-2][i+1] for i in range(len(triangle[n-2])-1)] + [Fraction(1)]]
		return triangle

def ComputeBernoulliArray(n, triangle=None):
	if n == 0:
		return [Fraction(1)]
	elif n >= 1:
		if triangle == None:
			triangle = PascalTriangle(n+2)
		bArray = ComputeBernoulliArray(n-1, triangle)
		if n % 2 > 0 and n > 1:
			return bArray + [Fraction(0)]
		bMultiply = np.array(triangle[n+1][0:n])
		bMultiply.shape = (n,1)
		bSum = np.dot(bArray, bMultiply)[0]
		bNumber = -bSum/triangle[n+1][n]
		return bArray + [bNumber]

#enter the n'th Bernoulli number you want to find
def bernoulli_number(n):
	if n % 2 > 0 and n > 1:
		return Fraction(0)
	else:
		return ComputeBernoulliArray(n)[n]

