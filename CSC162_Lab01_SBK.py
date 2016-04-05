# sarah kingan
# CSC162, summer2015
# Lab 01
#
# Original code Miller 
# http://interactivepython.org/runestone/static/pythonds/Introduction/
# ObjectOrientedProgramminginPythonDefiningClasses.html#a-fraction-class
#
# http://www.codeskulptor.org/#user40_vJPo8lLDq9_0.py

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# compare numerators using lowest common denominator
# of fraction
def numComp(a,b):
    first = a.num * b.den
    second = b.num * a.den
    return(first,second)

class Fraction:
    def __init__(self,top,bottom):
# Question 6
        if bottom < 0:
            bottom = abs(bottom)
            top = top * -1
        self.num = top
        self.den = bottom
# Question 2 - part A
        common = gcd(self.num,self.den)
        self.num = self.num/common
        self.den = self.den/common
        

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

# Question 2 - part B
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

# Question 1
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

# Question 3
    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    
    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    
    def __div__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum,newden)

# Question 4
    def __gt__(self,other):
        (first,second) = numComp(self,other)
        return first > second

    def __ge__(self,other):
        (first,second) = numComp(self,other)
        return first >= second

    def __lt__(self,other):
        (first,second) = numComp(self,other)
        return first < second

    def __le__(self,other):
        (first,second) = numComp(self,other)
        return first <= second

    def __ne__(self,other):
        (first,second) = numComp(self,other)
        return first != second
    
    

def main():
    print("Supply code tests")
    x = Fraction(1,-2)
    y = Fraction(2,3)
    print(str("fraction 1 is %s" % x))
    print(str("fraction 2 is %s" % y))
    print "Question 1 for fraction 1"
    print(x.getNum())
    print(x.getDen())
    print "Question 3" 
    print(x-y)
    print(x*y)
    print(x/y)
    print "Question 4"
    print(x>y)
    print(x>=y)
    print(x<y)
    print(x<=y)
    print(x!=y)
    
main()
