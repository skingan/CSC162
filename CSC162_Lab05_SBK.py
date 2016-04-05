# sarah kingan
# CSC162
# summer 2015
# LAB05
#
# some code from Miller and Ranum (2014)
# and from lecture 3 notes
#
# http://www.codeskulptor.org/#user40_m929ZLvYFY_21.py
#
# INSTRUCTIONS: Using your own doubly linked list class 
# rather than a Python listimplement a Stack.
#
# Test your stack by running the ballanced symbol checker
# example from the text.
#
# def parChecker(symbolString): 
# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))

class DNode:
    
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
        
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
    def setPrev(self,newprev):
        self.prev = newprev
    
    
class DLinkedList:
    
    def __init__(self):
        self.head = DNode()
        self.tail = DNode()
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)

    def printForward(self):
        current = self.head.getNext()
        while current != self.tail:
            print(current.getData())
            current = current.getNext()

    def printReverse(self):
        current = self.tail.getPrev()
        while current != self.head:
            print current.getData()
            current = current.getPrev()

    def addAtHead(self,item):
        tmp = DNode()
        tmp.setData(item)
        tmp.setPrev(self.head)
        tmp.setNext(self.head.getNext())
        self.head.getNext().setPrev(tmp)
        self.head.setNext(tmp)
        
    def addAtTail(self,item):
        tmp = DNode()
        tmp.setData(item)
        tmp.setNext(self.tail)
        tmp.setPrev(self.tail.getPrev())
        self.tail.getPrev().setNext(tmp)
        self.tail.setPrev(tmp)
                
    def popHead(self):
        if self.head.getNext() == self.tail:
            return None
        tmp = self.head.getNext()
        self.head.setNext(tmp.getNext())
        tmp.getNext().setPrev(self.head)
        return tmp.getData()
    
    def popTail(self):
        if self.tail.getPrev() == self.head:
            return None
        tmp = self.tail.getPrev()
        self.tail.setPrev(tmp.getPrev())
        tmp.getPrev().setNext(self.tail)
        return tmp.getData()

    def rmNode(self,node):
        node.getNext().setPrev(node.getPrev())
        node.getPrev().setNext(node.getNext())
    
    def remove(self,item):
        current = self.head.getNext()
        while current != self.tail:
            if current.getData() == item:
                self.rmNode(current)
                return current.getData()
            else:
                current = current.getNext()
        return None

        
        
class Stack:

    def __init__(self):
        self.dlist = DLinkedList()

    def isEmpty(self):
        return self.dlist.head.getNext() == self.dlist.tail

    def push(self, item):
        self.dlist.addAtHead(item)

    def pop(self):
        return self.dlist.popHead()

    def peek(self):
        return self.dlist.head.getNext().getData()

    def size(self):
        size = 0
        current = self.dlist.head.getNext()
        while current != self.dlist.tail:
            size = size +1
            current = current.getNext()
        return size
            
 
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(" or symbol == "{" or symbol == "[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{{([][])}()}'))

print(parChecker('[{()]'))
