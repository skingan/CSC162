# sarah kingan
# CSC162
# summer 2015
# LAB07
#
# 1. Write a recursive function to compute the factorial 
# of a number.
#
# 2. Write a recursive function to reverse a list.
#
# http://www.codeskulptor.org/#user40_pfTAlSDfsP_6.py

def factorial(n):
    if n<= 1: return 1
    return n * factorial(n-1)

def reverse(list):
    if len(list) == 1: return [list[0]]
    return reverse(list[1:]) + [list[0]]

def main():
    print(factorial(5))
    print(reverse(["A","B","C","D"]))
    
main()
          