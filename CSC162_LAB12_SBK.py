# sarah kingan
# CSC162, summer2015
# Lab 12
#
# Extend the buildParseTree function to handle mathematical 
# expressions that do not have spaces between every character.
#
# some code modified from Problem Solving with Algorithms 
# and Data Structures, By Brad Miller and David Ranum
#
# http://www.codeskulptor.org/#user40_8JkYKKrlnI_1.py


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
            
 
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
        
def buildParseTree(fpexp):
    fplist = addSpaces2mathExpr(fpexp).split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def addSpaces2mathExpr(string):
    newstring = string[0]
    if string[0].isdigit(): inNumber = True
    inNumber = False
    for i in range(1,len(string)):
        if not inNumber:
            newstring = newstring + ' ' + string[i]
            if string[i].isdigit():
                inNumber = True
        else:
            if string[i].isdigit():
                newstring = newstring + string[i]
            else:
                newstring = newstring + ' ' + string[i]
                inNumber = False
    return newstring

def evaluate(parseTree):

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        return doMath(parseTree.getRootVal(),evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
    
pt = buildParseTree("((100+50)*30)")
print evaluate(pt)
