#  File: htmlChecker.py
#  Description: This program goes through an HTML file and checks the tags.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/27/16
#  Date Last Modified:
#############################################################################
# create stack class
class Stack:

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

# function that creates tags
def getTags(f):
    tagList = []

    start = 0
    end = 0
    for lines in f:
        for i in range(len(lines)):
            if lines[i] == "<":
                start = i + 1
            elif lines[i] == ">":
                end = i
                tag = lines[start:end]
                if tag[0:4] == "meta":
                    tag = "meta"
                tagList.append(tag)
            else:
                pass              
    return(tagList)

#function that analyzes tags along with the exceptions
def analyzeTag(tagList):
    s = Stack()
    validTags = []
    exceptions = ["br", "meta", "hr"]
    for i in range(len(tagList)):
        if tagList[i][0] != "/":
            if tagList[i] in validTags:
                if tagList[i] in exceptions:
                    print("Tag is {} : does not need to match: stack is still {}".format(tagList[i],s))
                else:
                    s.push(tagList[i])
                    print("Tag is {} : pushed: stack is now {} \n".format(tagList[i], s))
            else:
                if tagList[i] in exceptions:
                    print("Tag is {} : does not need to match: stack is still {}".format(tagList[i],s))
                else:
                    s.push(tagList[i])
                    print("Tag is {} : pushed: stack is now {} \n".format(tagList[i], s))
        else:
            if s.peek() == tagList[i][1:]:
                s.pop()
                print("Tag is {} : matches: stack is now {} \n".format(tagList[i],s))
            else:
                print("Error:  tag is {} but top of stack is {}".format(tagList[i], s.peek()))
                return

    if s.isEmpty():
        print("Processing complete. No mismatches found.")
    else:
        print("Processing complete. Unmatched tags remain on stack: {}".format(s))

       
def main():
    # open the file htmlfile.txt
    f = open ("htmlfile.txt", "r")

    tagSet = getTags(f)
    print(tagSet)

    analyzingTags = analyzeTag(tagSet)

    # close file
    f.close()
    
main()
