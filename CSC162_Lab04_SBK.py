# sarah kingan
# CSC162
# Summer 2015
# LAB04
#
# some code from Miller and Ranum (2014)
# and from lecture 3 notes
#
# http://www.codeskulptor.org/#user40_enQAsuootn_3.py
#
# Implement your own doubly  linked list class 
# (a linked list with links in both directions) 
# using your own Node class (with a 'next' and a 
# 'previous' link).
# 
# Your linked list class should have both a "head" 
# and a "tail"
#
# Your class should support "addAtHead(item)" and 
# "popHead()" and "addAtTail(item)" and "popTail()" 
# and "printForward()" and "printReverse()" and 
# "remove(item)"
#
# Test your class by inserting some items, printing 
# in both directions removing an item then printing again.


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

        
        
        
def main():

    print "**set up linked list**"
    family = DLinkedList()
    family.addAtHead('sarah')
    family.addAtHead('simone')    
    family.addAtTail('adeline')
    family.addAtTail('dan')
    family.addAtTail('oma')
    family.addAtHead('papa')
    print "**print it forward**"
    family.printForward()
    print "**pop head, print returned value**"
    print family.popHead()
    print "**print list in reverse**"
    family.printReverse()
    print "**remove 'simone' and print returned value**"
    print family.remove('simone')
    print "**print list forward**"
    family.printForward()
    print "**pop tail, print returned value**"
    print family.popTail()
    print "**print final list in reverse**"
    family.printReverse()

main()
            
            
            