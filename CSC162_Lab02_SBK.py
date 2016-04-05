# sarah kingan
# CSC162, summer2015
# Lab 02
#
# http://www.codeskulptor.org/#user40_LrUfzPLoH3_6.py
#
# A program that compares the performance of the del
# function for lists and dictionaries

import time

# make an arbitary dictionary of user specified size
def dict(n):
    dict = {}
    a = range(n)
    for i in a:
        dict[i] = 1
    return dict

# make an arbitrary list of user specified length
def list(n):
    list = []
    a = range(n)
    for i in a:
        list.append(i)
    return list



# time the deletion of all items in dictionary
def time2delDict(n):
    
    d = dict(n)
    k = d.keys()
    
    start = time.time()
    
    for key in k:
        del d[key]
        
    end = time.time()
    
    return end-start

# time the deletion of all items in a list
def time2delList(n):
    
    l = list(n)
    
    start = time.time()
    
    while len(l) > 0:
        del l[0]
    
    end = time.time()

    return end-start

# create 3 arrays that can be used to study the performance
# of del for lists and dictionaries
# given different size data inputs
dataSize = []
listTime = []
dictTime = []
# the upper limit and step size should be higher for a real analysis
# for example: range(100,1000000,5000)
# the values implemented below are chosen due to the contraints of
# runtime in codeskuplter
for i in range(1000,10000,500):
    dataSize.append(i)
    listTime.append(time2delList(i))
    dictTime.append(time2delDict(i))

print dataSize
print dictTime
print listTime

