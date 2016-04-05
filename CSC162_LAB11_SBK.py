# sarah kingan
# CSC162, summer2015
# Lab 11
#
# Implement the median-of-three method for selecting 
# a pivot value as a modification to quickSort. 
# Run an experiment to compare the two techniques.
#
# Code modified from Problem Solving with Algorithms 
# and Data Structures, By Brad Miller and David Ranum
#
# http://www.codeskulptor.org/#user40_48M8k01fnt_3.py
#

import codeskulptor
codeskulptor.set_timeout(1000)

# add two pivot functions that return the index of the pivot rather than the value
def pivotFirst(alist,first,last):
    return first

def pivotMedian(alist,first,last):
    if ((alist[first] - alist[last]) * (alist[(last-first)/2] - alist[first])) >= 0:
        return first
    elif ((alist[last] - alist[first]) * (alist[(last-first)/2] - alist[last])) >= 0:
        return last
    else:
        return (last-first)/2

# all functions must not take pivot function as argument
def quickSort(alist, pivotFunction):
   quickSortHelper(alist,0,len(alist)-1,pivotFunction)

def quickSortHelper(alist,first,last,pivotFunction):
   if first<last:

       splitpoint = partition(alist,first,last,pivotFunction)

       quickSortHelper(alist,first,splitpoint-1,pivotFunction)
       quickSortHelper(alist,splitpoint+1,last,pivotFunction)


def partition(alist,first,last,pivotFunction):

# obtain pivot index for pivot function chosen
   pivotindex = pivotFunction(alist,first,last)
# if the median function is chosen, 
# swap the pivot into the first position
   if (pivotFunction == 'pivotMedian'):
        temp = alist[first]
        alist[first] = alist[pivotindex]
        alist[pivotindex] = temp
        
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

# when comparing values to the pivot, 
# use the pivot index, which is always first
       while leftmark <= rightmark and \
               alist[leftmark] <= alist[first]:
           leftmark = leftmark + 1

       while alist[rightmark] >= alist[first] and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def random_list(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l

def mean(alist):
    sum = 0
    for i in range(0,len(alist)):
        sum = sum + alist[i]
    return float(sum)/len(alist)


def timeSort(alist, pivotFunction):
    
    import time

    start = time.time()
    quickSort(alist,pivotFunction)
    end = time.time()
    return end-start


#alist = [54,26,93,17,77,31,44,55,20]
#blist = [54,26,93,17,77,31,44,55,20]
#print(blist)
#quickSort(alist, pivotFirst)
#print(alist)
#quickSort(blist, pivotMedian)
#print(blist)

# run an experiment on a list of 1000 random numbers
# replicate experiment 1000 times
# (This requires increasing the runtime limits
# of codeskulptor)
firstTimes = []
medianTimes = []
for i in range(1000):
    alist = random_list(1000)
    blist = alist[:]
    firstTimes.append(timeSort(blist,pivotFirst))
    medianTimes.append(timeSort(alist,pivotMedian))
print mean(firstTimes)
print mean(medianTimes)
# suprisingly, median takes ~10% longer than first!!



