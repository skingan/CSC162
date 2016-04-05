# sarah kingan
# LAB03
# 
# a program to print the kth smallest item in a random
# list of numbers
#
# uses the python2 list sort function which runs in
# nlogn time (Table 2, Miller and Ranum, Analysis chapter)
#
# http://www.codeskulptor.org/#user40_iceeZVwUe5_1.py
#

# create list of (pseudo)random numbers
# of user-specified length
# random numbers are floats that range between 0 and 1
def random_list(n):
    import random
    l = []
    for i in range(n):
        l.append(random.random())
    return l

# sort list using pythons default sorting function
# return the kth smallest number
def kth_smallest(list,k):
    list.sort()
    return list[k]    
    

# create list of 1000 random numbers    
x = random_list(1000)
# print 25th smallest number
print kth_smallest(x,25)

