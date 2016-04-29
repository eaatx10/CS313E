#  File: ExpressionTree.py
#  Description: 
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 4/18/16
#  Date Last Modified: 
#############################################################################
class BinaryTree (object):

    def BinaryTree(initdata):
        return([initdata,[],[]])

    def _init__(self, initValue):
        self.root = "&"
        self.data = initValue
        self.parent = None
        self.left = None
        self.right = None
        

    def getRootVal(t):
        return(t[0])

    def setRootVal(t, value):
        t[0] = value

    def getLeftChild(t):
        return(t[1])

    def getRightChild(t):
        return (t[2])

    def insertLeft(root, newBranch):
        temp = root.pop(1)
        root.insert(1,[newBranch, temp, []])

    def insertRight(root, newBranch):
        temp = root.pop(2)
        root.insert(2, [newBranch, [], temp])

class Stack (object):

    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return(self.items[-1])

    def isEmpty(self):
        return(self.items == [])

    def size(self):
        return(len(self.items))


def createTree(self):
    s = Stack()
    inputExpr = str(input("Infix expression: "))
    mathExpr = inputExpr.split()

    for token in mathExpr:
        if token == ")":
            currentNode = current.parentNode
            if not s.isEmpty():
                s.pop()
        elif token == "(":
            newNode = BinaryTree("&")
            insertLeft(newNode)
            s.push(currentNode)
            currentNode = newNode
        elif token in operators:
            currentNode.data = token
            s.push(currentNode)
            newNode = BinaryTree("&")
            insertRight(newNode)
            currentNode = newNode
        else:
            currentNode.data = token
            currentNode = current.parentNode
            s.pop()

def evaluate()

def main():

    # open file
    file = open("treedata.txt", "r")
    lineOne = file.readlines()

    global operators
    operators = ['+', '-', '*', '/']

    #close file



main()
