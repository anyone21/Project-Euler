# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 10:01:47 2016

@author: wxt
"""

"""
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import math

def euclidean(x, y):
    
    assert x > 0, y > 0
    
    if x < y:
        x, y = y, x
    
    mod = x % y
    while mod != 0:
        x, y = y, mod
        mod = x % y
    
    return y

def findtriplet(condition):
    
    # a + b + c = 2km(m+n)
    # so, m < sqrt((a+b+c)/2)
    maxiter = int(math.sqrt(condition/2.))
    for n in range(1, maxiter + 1):
        for m in range(n+1, maxiter + 1):
            mod = euclidean(m, n)
            if (mod == 1) and ((m - n) % 2 != 0): # conditions for primitive solutions
                k = 1
                while True:
                    # Use the Euclid's foluma to generate Pythagorean triplets
                    a = k * (m**2 - n**2)
                    b = 2 * m * n * k
                    c = k * (m**2 + n**2)
                    if a + b + c > condition:
                        break
                    if a + b + c == condition:
                        return a * b * c
                    k += 1 # non primitive triplets?
    
    return
        

if __name__ == '__main__':
    
    print(findtriplet(1000))
            