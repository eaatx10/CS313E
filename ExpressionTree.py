#  File: ExpressionTree.py
#  Description: This file reads arithmetic expressions from an input file and creates expression trees, structures that store the expressions using an infix traversal method.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
# 
#############################################################################
class BinaryTree (object):

    def __init__(self, initValue, parent = None):
        self.data = initValue
        self.parent = parent
        self.left = None
        self.right = None
        
    def getRootVal(self):
        return(self.data)
    
    def setRootVal(self, value):
        self.data = value

    def getLeftChild(self):
        return(self.left)

    def getRightChild(self):
        return(self.right)

    def insertLeft(self, newBranch, parent = None):
        if self.left == None:
            self.left = BinaryTree(newBranch, parent)
        else:
            temp = BinaryTree(newBranch, parent)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newBranch, parent = None):
        if self.right == None:
            self.right = BinaryTree(newBranch, parent)
        else:
            temp = BinaryTree(newBranch, parent)
            temp.right = self.right
            self.right = temp

    # calculate expression value
    def evaluate(self):
        currentNode = self
        if currentNode.getRootVal() in operators:
            operand1 = currentNode.getLeftChild()
            operand2 = currentNode.getRightChild()

            # call the method on itself
            leftOperand = operand1.evaluate()
            rightOperand = operand2.evaluate()
            operator = currentNode.getRootVal()
            
            expression = "{}{}{}".format(leftOperand, operator, rightOperand)
            result = eval(expression)
        # base case
        else:
            result = currentNode.getRootVal()
        return(result)

    def createTree(self, expression):
        s = Stack()
        inputExpr = expression
        mathExpr = inputExpr.split()
        currentNode = self

        for token in mathExpr:
            if token == ")":
                currentNode = currentNode.parent
                if not s.isEmpty():
                    s.pop()
            elif token == "(":
                currentNode.insertLeft("&", parent = currentNode)
                s.push(currentNode)
                currentNode = currentNode.getLeftChild()
            elif token in operators:
                currentNode.setRootVal(token)
                s.push(currentNode)
                currentNode.insertRight("&", parent = currentNode)
                currentNode = currentNode.getRightChild()
            else:
                currentNode.setRootVal(token)
                currentNode = currentNode.parent
                s.pop()

    # prefix notation
    def preOrder(currentNode):
        preList = []
        if currentNode.data in operators:
            preList.append(currentNode.data)
            preList.append(currentNode.getLeftChild().preOrder())
            preList.append(currentNode.getRightChild().preOrder())
        else:
            preList.append(currentNode.data)
        return " ".join(preList)

    # postfix notation
    def postOrder(currentNode):
        postList = []
        if currentNode.data in operators:
            postList.append(currentNode.getLeftChild().postOrder())
            postList.append(currentNode.getRightChild().postOrder())
            postList.append(currentNode.data)
        else:
            postList.append(currentNode.data)
        return " ".join(postList)


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

    def __str__(self):
        return(str(self.items))

def main():

    # open file
    file = open("treedata.txt", "r")
    lines = file.readlines()

    global operators
    operators = ['+', '-', '*', '/']

    # print ouput and call methods
    for line in lines:
        expression = line
        exTree = BinaryTree("&")
        exTree.createTree(expression)
        answer = exTree.evaluate()

        print("Infix expression: {}\n".format(expression.rstrip("\n")))
        print("   Value: {}".format(answer))
        print("   Prefix expression: {}".format(exTree.preOrder()))
        print("   Postfix expression: {}\n".format(exTree.postOrder()))
    
    #close file
    file.close()

    

main()
