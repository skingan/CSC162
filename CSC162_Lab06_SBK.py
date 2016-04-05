# sarah kingan
# CSC162
# summer 2015
# LAB06
#
# some code from Miller and Ranum (2014)
# and from lecture 3 notes
#
# http://www.codeskulptor.org/#user40_m929ZLvYFY_24.py
#
# INSTRUCTIONS: Using your own doubly linked list class 
# rather than a Python list implement a Queue.
#
# Test your stack by running the hotpotato simulation 
# from the text.
#
# def hotPotato(namelist, num):

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

        
        
class Queue:

    def __init__(self):
        self.dlist = DLinkedList()

    def isEmpty(self):
        return self.dlist.head.getNext() == self.dlist.tail

    def enqueue(self, item):
        self.dlist.addAtHead(item)

    def dequeue(self):
        return self.dlist.popTail()

    def size(self):
        size = 0
        current = self.dlist.head.getNext()
        while current != self.dlist.tail:
            size = size +1
            current = current.getNext()
        return size
            
        
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
