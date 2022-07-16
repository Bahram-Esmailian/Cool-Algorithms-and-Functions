#Double Linear Algorithm created and written by Bahram Esmailian

import numpy as np

def y(n): return n*2+1

def z(n): return n*3+1

def dbl_linear(n):
    if n == 0:
        return 1
#Find the generaton in which the number was created, i.e. U(3) was created in the 2nd generation. Therefore we subtract the lengths of each generation until we have a length that is greater than or equal to our number.
#We subtract the number of products in each generation from the initial number so that we "Index" it, i.e (n - products in gen 0) - (products in gen 1) = 3-(1)-(2) = 0 which is the position 
#of U(3) with respect to the 2nd generation like such: [U(3), U(4), U(5), U(4)] and the 0th index of this matrix will be U(3). This is done because we gain important information as now 
#we can trace back the numbers' lineage.
    else:
        gen = 0
        while n > 2**gen:
            n = n-2**gen
            gen += 1
    matrix = np.empty(gen)
#The an interesting pattern pops out from the mathematics, the left most number or, the smallest number in a generation has only undergone the y = 2x + 1 function. The right most number, or
#the largest number in a generation has only undergone the z = 3x + 1 function. We can find the lineage of these numbers easily now but how about the numbers in between? Well their lineage can also be
#inferred from their position. The 2nd smallest number undergoes first a z function and then 1 y function, we can make a list representing this lineage [z,y] in order from first to last function applied
#the 2nd largest function's list looks like [y,z]
#The pattern is hard to spot in the 2nd generation so lets observe the 3rd generation:
#Index: List
#0:[y,y,y]
#1:[z,y,y]
#2:[y,z,y]
#3:[y,y,z]
#4:[z,z,y]
#5:[z,y,z]
#6:[y,z,z]
#7:[z,z,z]
#observe the distinct pattern from 0-3, the z function going from earliest to latest function
#from 3-4 the two lists are opposite of eachother and note how this changes as we go from the lower half of the numbers to the larger half of the numbers
#observe the pattern from 4-7 as the y function moves from last to first in order of execution before it disappears
    if n < 2**gen/2:
        matrix[::] = 0
        if n == 0:
            return matrix
        else:
            matrix[n-1] = 1
            return matrix 
    else:
        matrix[::] = 1
        if n == 2**gen-1:
            return matrix
        else:
            matrix[2**gen-n-2] = 0
            return matrix

print(dbl_linear(9))
    
        
