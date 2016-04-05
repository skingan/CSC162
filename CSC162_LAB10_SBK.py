# sarah kingan
# CSC162, summer2015
# Lab 10
#
# Using a random number generator, create a list of 500 
# integers. Perform a benchmark analysis of:
# Bubblesort
# InsertionSort
# Selectionsort
# Shellsort
# Mergesort
# Quicksort 
# What is the difference in execution speed?
#
# Code modified from Problem Solving with Algorithms 
# and Data Structures, By Brad Miller and David Ranum
#
# http://www.codeskulptor.org/#user40_pAX0Ncn0Uu_13.py
#

import codeskulptor
codeskulptor.set_timeout(1000)

######################################################
# BUBBLE SORT
######################################################
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

    
######################################################
# SELECTION SORT
######################################################    
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
    
    
######################################################
# INSERTION SORT
######################################################    
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

    
######################################################
# SHELL SORT
######################################################    
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
        
        
######################################################
# MERGE SORT
######################################################            
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    
    
######################################################
# QUICK SORT
######################################################                
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
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


######################################################
# OTHER FUNCTIONS
######################################################                
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


####################################################

import time

methods = ['shortBubbleSort', 'selectionSort', \
           'insertionSort', 'shellSort', 'mergeSort', \
           'quickSort']
times = [[] for i in range(6)]

# 100 trials per method
for n in range(20):
    alist = random_list(600)    
    for i in range(len(methods)):
# i couldn't figure out a way to call a method in a function
# as a string. I know the following code is inelegant
# but it gets the job done.
        blist = alist[:]
        if i == 0:
            start = time.time()
            shortBubbleSort(blist)        
            end = time.time()
            times[i].append(end - start)
        elif i == 1:
            start = time.time()
            selectionSort(blist)        
            end = time.time()
            times[i].append(end - start)
        elif i == 2:
            start = time.time()
            insertionSort(blist)        
            end = time.time()
            times[i].append(end - start)
        elif i == 3:
            start = time.time()
            shellSort(blist)        
            end = time.time()
            times[i].append(end - start)
        elif i == 4:
            start = time.time()
            mergeSort(blist)        
            end = time.time()
            times[i].append(end - start)
        elif i == 5:
            start = time.time()
            quickSort(blist)        
            end = time.time()
            times[i].append(end - start)

for i in range(len(methods)):
    print (methods[i], mean(times[i]))
        
 
# output for lists of length 500 and 100 trials
# ('shortBubbleSort', 0.457519984245)
# ('selectionSort', 0.232360010147)
# ('insertionSort', 0.346949999332)
# ('shellSort', 0.0353600096703)
# ('mergeSort', 0.0644099879265)
# ('quickSort', 0.0348700118065)
 
        
# The order of sorting methods from worst to best are:
# bubble, insertion, selection, merge, shell, quick
# the latter three methods are an order of magnitude faster
# than the former.
    
