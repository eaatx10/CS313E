#  File: ERsim.py
#  Description: 
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#############################################################################
# create queue
class Queue:
    def __init__ (self):
        self.items = []
    def __str__ (self):
        return(str(self.items))
    def isEmpty (self):
        return (self.items == [])
    def enqueue (self,item):
        self.items.insert(0,item)
    def dequeue (self):
        return (self.items.pop())
    def size (self):
        return (len(self.items))
    def peek(self):
        return(self.items[-1])

# function that treats next patient 
def treatNext (criticalPatients, seriousPatients, fairPatients):
    
    if not criticalPatients.isEmpty():
        criticalPatients.dequeue()
        if not seriousPatients.isEmpty():
            seriousPatients.dequeue()
            if not fairPatients.isEmpty():
                fairPatients.dequeue()
            else:
                print("No patients are available to treat.")
    print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {} \n".format(criticalPatients,seriousPatients,fairPatients))

# function that treats next patient based upon condition
def treatCondition (condition, strCondition):
    
    print("Treating {} from {} queue".format(condition.peek(), strCondition))
    condition.dequeue()

# function that treats all patients in each queue
def treatAll (criticalPatients, seriousPatients, fairPatients):

    while not criticalPatients.isEmpty():
        print("Treating {} from Critical queue".format(criticalPatients.peek()))
        criticalPatients.dequeue()
        print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {}".format(criticalPatients,seriousPatients,fairPatients))
    while not seriousPatients.isEmpty():
        print("Treating {} from Serious queue".format(seriousPatients.peek()))
        seriousPatients.dequeue()
        print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {}".format(criticalPatients,seriousPatients,fairPatients))
    while not fairPatients.isEmpty():
        print("Treating {} from Fair queue".format(fairPatients.peek()))
        fairPatients.dequeue()
        print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {}".format(criticalPatients,seriousPatients,fairPatients))
    print ("No patients in queues.")
           
def main():

# open the file ERsim.txt
    f = open ("ERsim.txt", "r")

    criticalPatients = Queue()
    seriousPatients = Queue()
    fairPatients = Queue()
    
    # split line and add patients to each queue
    for line in f:
        line = line.split()
        if line[0] == "add":
            if line[2] == "Critical":
                criticalPatients.enqueue(line[1])
            elif line[2] == "Serious":
                seriousPatients.enqueue(line[1])
            else:
                fairPatients.enqueue(line[1])
            print("Add patient {} to {} queue".format(line[1], line[2]))
            print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {} \n".format(criticalPatients,seriousPatients,fairPatients))

        # call treatCondition, treatNext, treatAll functions
        elif line[0] == "treat":
            print ("Treating {} patient(s).\n".format(line[1]))
            if line[1] == "next":
                treatNext(criticalPatients, seriousPatients, fairPatients)
            elif (line[1] != "all"):
                if line[1] == "Critical":
                    treatCondition (criticalPatients, "Critical")
                elif line[1] == "Serious":
                    treatCondition (seriousPatients, "Serious")
                elif line[1] == "Fair":
                    treatCondition (fairPatients, "Fair")
                print("Queues are: \n Critical: {} \n Serious: {} \n Fair: {} \n".format(criticalPatients,seriousPatients,fairPatients))
            else:
                treatAll (criticalPatients, seriousPatients, fairPatients)
         
        elif line[0] == "exit":
            print("Exit")
            break

    # close file
    f.close()

main()
