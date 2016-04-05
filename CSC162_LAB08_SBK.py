# sarah kingan
# CSC162
# summer 2015
# LAB08
#
# Write a recursive function to compute the Fibonacci 
# sequence. How does the performance of the recursive 
# function compare to that of an iterative version?
#
# http://www.codeskulptor.org/#user40_a09EvnV82b_3.py
#
#
#
import time

def FibRec(n):
    if n <= 2: return 1
    return FibRec(n-1) + FibRec(n-2)

def FibIt(n):
    fibTable = [0,1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1] + fibTable[i-2])
    return fibTable[n]

def timeIt(function,n):
    start = time.time()
    function(n)
    end = time.time()
    return end - start
    

def main():
    print("\t".join(["n","Recursion","Iteration"]))
    for n in range(10,30,2):
        recTime = timeIt(FibRec,n)
        itTime = timeIt(FibIt,n)
        print ("\t".join([str(n),str(recTime),str(itTime)]))
    
main()


