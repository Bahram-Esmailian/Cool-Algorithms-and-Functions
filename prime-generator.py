#Fast Prime Generator created and written by Bahram Esmailian
#this algorithm implements the Seive of Eratosthenes is one of the fastest algorithms for generating prime numbers

#let n be the upper limit of primes generated
n = 100000
numbers = []

for i in range(n+1):
    numbers = numbers + [i]

p = 2
while p*p <= n+1:
    for j in range(p*p,n+1,p):
        numbers[j] = 0 
    if p != 2:
        p += 2
        if p not in numbers:
            p += 2

    else:
        p += 1

primes = []

for n in numbers:
    if n != 0:
        primes = primes + [n]
        
print(primes)
