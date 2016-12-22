#  File: Scheduler.py
#  Description: This program is an algorithm to run a multiple feedback queue.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#############################################################################
# create queue
class Queue:
    def __init__ (self):
        self.head = None
        self.tail = self.head
    def __str__ (self):
        return(str(self.items))
    def isEmpty (self):
        return self.head == None 
    def enqueue (self,node):
        node.setNext(None)
        if (self.isEmpty()):
            self.head = node
            self.tail = self.head
        else:
            self.tail.setNext(node)
            self.tail = node    
    def dequeue (self):
        old = self.head
        self.head = old.getNext()
        return (old)
    def size (self):
        return (len(self.items))
    def peek(self):
        return (self.head)
    def __str__(self):
        current = self.head
        result = ""
        while current != None:
            result += "->[P"
            result += str(current.getProcess_id())
            result += "]"
            current = current.getNext()
        return result

# create process
class Process (object):
    def __init__ (self, process_id, duration, IOTimeStamp):
        self.process_id = process_id
        self.duration = duration
        self.IOTimeStamp = IOTimeStamp

    def getProcess_id (self):
        return self.process_id

    def getDuration (self):
        return  self.duration

    def getNextIOTime (self):
        if (len(self.IOTimeStamp) == 0):
            return -1
        else:
            return self.IOTimeStamp.pop(0)

# create node
class Node (object):
    def __init__(self, process_id, time_left, nextIO):
        self.process_id = process_id
        self.time_left = time_left
        self.nextIO = nextIO
        self.currentTime = 0
        self.next = None

    def getProcess_id (self):
        return self.process_id

    def getTimeLeft (self):
        return self.time_left

    def getNextIO (self):
        return self.nextIO

    def getCurrentTime (self):
        return self.currentTime

    def getNext (self):
        return self.next

    def setTimeLeft (self, newTimeLeft):
        self.time_left = newTimeLeft

    def setCurrentTime (self, updateCurrent):
        self.currentTime = updateCurrent

    def setIO (self, updateIO):
        self.nextIO = updateIO

    def setNext (self, updateNext):
        self.next = updateNext

    def __str__ (self):
        return str(self.process_id)

# create scheduler
class Scheduler(object):
    def __init__ (self):
        self.top = Queue()
        self.mid = Queue()
        self.bot = Queue()
        self.time = 0
        self.proDict = {}
        self.resultProcess = []

    def addToResult(self, process_id, time):
        self.resultProcess.append("->P" + str(process_id) +"(" + str(time) + ")")

    def takeProcesses (self, process_list):
        # create dict, node, and add node to top level queue
        for p in process_list:
            self.proDict[p.getProcess_id()] = p
            node = Node (p.getProcess_id(), p.getDuration(), p.getNextIOTime())
            self.top.enqueue(node)

    def run(self):
        while((not self.top.isEmpty()) or (not self.mid.isEmpty()) or (not self.bot.isEmpty())):
            if (not self.top.isEmpty()):
                temp = self.top.dequeue()
                time_slice = 10
                # check for IO
                if ((temp.getNextIO() != -1) and temp.getNextIO() <= time_slice + temp.getCurrentTime()):
                    diff = temp.getNextIO() - temp.getCurrentTime()
                    self.addToResult(temp.getProcess_id(), diff)
                    self.time += diff

                    temp.setCurrentTime(temp.getNextIO())
                    temp.setTimeLeft(temp.getTimeLeft() - diff)

                    p = self.proDict[temp.getProcess_id()]

                    temp.setIO(p.getNextIOTime())
                    self.top.enqueue(temp)

                # check if process finishes within timeslice
                elif (temp.getTimeLeft() <= time_slice):
                    self.addToResult(temp.getProcess_id(), temp.getTimeLeft())
                    self.time += temp.getTimeLeft()

                else:
                    self.addToResult(temp.getProcess_id(), time_slice)
                    self.time += time_slice

                    temp.setTimeLeft(temp.getTimeLeft() - time_slice)
                    temp.setCurrentTime(temp.getCurrentTime() + time_slice)

                    self.mid.enqueue(temp)

            elif (not self.mid.isEmpty()):
                temp = self.mid.dequeue()
                time_slice = 100
                # check for IO
                if ((temp.getNextIO() != -1) and (temp.getNextIO()) <= time_slice + temp.getCurrentTime()):
                    diff = temp.getNextIO() - temp.getCurrentTime()
                    self.addToResult(temp.getProcess_id(), diff)
                    self.time += diff

                    temp.setCurrentTime(temp.getNextIO())
                    temp.setTimeLeft(temp.getTimeLeft() - diff)

                    p = self.proDict[temp.getProcess_id()]

                    temp.setIO(p.getNextIOTime())
                    self.top.enqueue(temp)

                # check if process finishes within timeslice
                elif (temp.getTimeLeft() <= time_slice):
                    self.addToResult(temp.getProcess_id(), temp.getTimeLeft())
                    self.time += temp.getTimeLeft()

                else:
                    self.addToResult(temp.getProcess_id(), time_slice)
                    self.time += time_slice

                    temp.setTimeLeft(temp.getTimeLeft() - time_slice)
                    temp.setCurrentTime(temp.getCurrentTime() + time_slice)

                    self.bot.enqueue(temp)
            else:
                temp = self.bot.dequeue()
                time_slice = 1000
                # check for IO
                if ((temp.getNextIO() != -1) and (temp.getNextIO()) <= time_slice + temp.getCurrentTime()):
                    
                    diff = temp.getNextIO() - temp.getCurrentTime()
                    self.addToResult(temp.getProcess_id(), diff)
                    self.time += diff

                    temp.setCurrentTime(temp.getNextIO())
                    temp.setTimeLeft(temp.getTimeLeft() - diff)

                    p = self.proDict[temp.getProcess_id()]

                    temp.setIO(p.getNextIOTime())
                    self.mid.enqueue(temp)

                # check if process finishes within timeslice
                elif (temp.getTimeLeft() <= time_slice):
                    self.addToResult(temp.getProcess_id(), temp.getTimeLeft())
                    self.time += temp.getTimeLeft()

                else:
                    self.addToResult(temp.getProcess_id(), time_slice)
                    self.time += time_slice

                    temp.setTimeLeft(temp.getTimeLeft() - time_slice)
                    temp.setCurrentTime(temp.getCurrentTime() + time_slice)

                    self.bot.enqueue(temp)

        self.printResultingSchedule()

    def printResultingSchedule(self):
        result = ""
        count = 0
        print("Resulted Schedule:")
        for s in self.resultProcess:
            result += s
            count += 1
            if count % 5 == 0:
                result += "\n"
        print (result)

def main ():
    # open file
    fh = open("Processes.txt","r")
    process_list = []
    scheduler = Scheduler()

    # read through file
    for line in fh:
        data = line.strip().split(";")
        process_list.append(Process(int(data[0]),int(data[1]),eval(data[2])))

    scheduler.takeProcesses(process_list)
    scheduler.run()

main()
    

        

    
        
        
