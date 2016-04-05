# sarah kingan
# CSC162
# summer 2015
# LAB09
#
# Write a program that prints out Pascal’s triangle. 
# Your program should accept a parameter that tells 
# how many rows of the triangle to print.
#
# http://www.codeskulptor.org/#user40_ftWr5NCSh9_1.py

def PascalsT(n):
    if n == 1: return [[1]]
    L = [1]
    for i in range(1,n-1):
        L.append(PascalsT(n-1)[n-2][i-1] + PascalsT(n-1)[n-2][i])
    L.append(1)
    return PascalsT(n-1) + [L]
   
output = PascalsT(6)
for i in range(0,len(output)):
    print output[i]
        
