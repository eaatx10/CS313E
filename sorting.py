#  File: numberPath.py
#  Description: This program executes a drive that sorts various lists using different sorting algorithms, all while recording each execution time in a table of results. 
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
# 
#############################################################################
import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
#############################################################################
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

#############################################################################
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
#############################################################################
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue
#############################################################################
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
#############################################################################
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
###############################################################################
#function to calculate average times for the 3 different n
def randomTesting (n):
    #bubble sort timing
    timingAverages10 = []
    timingAverages100 = []
    timingAverages1000 = []

    while (n <= 1000):
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #insertion sort timing
        
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #selection sort timing
        
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
            
        #shell sort timing
        
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #merge sort timing
        
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)


        #quick sort timing
        
        avg = 0
        #shuffle list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
        n = n * 10

    #"Random" input/output
    print("\nInput type = Random") 
    print("                   avg time   avg time   avg time") 
    print("   Sort function    (n=10)     (n=100)   (n=1000)") 
    print("-----------------------------------------------------")
    print("      bubbleSort   {}   {}   {}".format(timingAverages10[0],timingAverages100[0], timingAverages1000[0]))
    print("   selectionSort   {}   {}   {}".format(timingAverages10[2],timingAverages100[2], timingAverages1000[2]))
    print("   insertionSort   {}   {}   {}".format(timingAverages10[1],timingAverages100[1], timingAverages1000[1]))
    print("       shellSort   {}   {}   {}".format(timingAverages10[3],timingAverages100[3], timingAverages1000[3]))
    print("       mergeSort   {}   {}   {}".format(timingAverages10[4],timingAverages100[4], timingAverages1000[4]))
    print("       quickSort   {}   {}   {}".format(timingAverages10[5],timingAverages100[5], timingAverages1000[5]))
###############################################################################
def sortedTesting (n):
    #bubble sort timing
    timingAverages10 = []
    timingAverages100 = []
    timingAverages1000 = []

    while (n <= 1000):
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #insertion sort timing
        
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #selection sort timing
        
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
            
        #shell sort timing
        
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #merge sort timing
        
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)


        #quick sort timing
        
        avg = 0
        #calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
        n = n * 10

    #"Sorted" input/output
    print("\nInput type = Sorted") 
    print("                   avg time   avg time   avg time") 
    print("   Sort function    (n=10)     (n=100)   (n=1000)") 
    print("-----------------------------------------------------")
    print("      bubbleSort   {}   {}   {}".format(timingAverages10[0],timingAverages100[0], timingAverages1000[0]))
    print("   selectionSort   {}   {}   {}".format(timingAverages10[2],timingAverages100[2], timingAverages1000[2]))
    print("   insertionSort   {}   {}   {}".format(timingAverages10[1],timingAverages100[1], timingAverages1000[1]))
    print("       shellSort   {}   {}   {}".format(timingAverages10[3],timingAverages100[3], timingAverages1000[3]))
    print("       mergeSort   {}   {}   {}".format(timingAverages10[4],timingAverages100[4], timingAverages1000[4]))
    print("       quickSort   {}   {}   {}".format(timingAverages10[5],timingAverages100[5], timingAverages1000[5]))
###############################################################################
def shuffledTesting (n):
    #bubble sort timing
    timingAverages10 = []
    timingAverages100 = []
    timingAverages1000 = []

    while (n <= 1000):
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #insertion sort timing
        
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #selection sort timing
        
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
            
        #shell sort timing
        
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #merge sort timing
        
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)


        #quick sort timing
        
        avg = 0
        #reverse list and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            myList.reverse()
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
        n = n * 10

    #"Reverse" input/output
    print("\nInput type = Reverse ") 
    print("                   avg time   avg time   avg time") 
    print("   Sort function    (n=10)     (n=100)   (n=1000)") 
    print("-----------------------------------------------------")
    print("      bubbleSort   {}   {}   {}".format(timingAverages10[0],timingAverages100[0], timingAverages1000[0]))
    print("   selectionSort   {}   {}   {}".format(timingAverages10[2],timingAverages100[2], timingAverages1000[2]))
    print("   insertionSort   {}   {}   {}".format(timingAverages10[1],timingAverages100[1], timingAverages1000[1]))
    print("       shellSort   {}   {}   {}".format(timingAverages10[3],timingAverages100[3], timingAverages1000[3]))
    print("       mergeSort   {}   {}   {}".format(timingAverages10[4],timingAverages100[4], timingAverages1000[4]))
    print("       quickSort   {}   {}   {}".format(timingAverages10[5],timingAverages100[5], timingAverages1000[5]))
###############################################################################
def almostTesting (n):
    #bubble sort timing
    timingAverages10 = []
    timingAverages100 = []
    timingAverages1000 = []

    while (n <= 1000):
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #insertion sort timing
        
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #selection sort timing
        
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
            
        #shell sort timing
        
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)

        #merge sort timing
        
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
        
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)


        #quick sort timing
        
        avg = 0
        #create 'almost list' and calculate average
        for i in range (5):
            myList = [i for i in range (n)]
            
            for i in range (n // 10):
                index1 = random.randint(0, n-1)
                index2 = random.randint(0, n-1)

                temp = myList[index1]
                myList[index1] = myList[index2]
                myList[index2] = temp
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            avg += elapsedTime

        #format averages
        avg = round(avg / 5,6)
        if n == 1000:
            timingAverages1000.append("%.6f" % avg)
        elif n == 100:
            timingAverages100.append("%.6f" % avg)
        else:
            timingAverages10.append("%.6f" % avg)
        n = n * 10

    #"Almost sorted" input/output
    print("\nInput type = Almost sorted ") 
    print("                   avg time   avg time   avg time") 
    print("   Sort function    (n=10)     (n=100)   (n=1000)") 
    print("-----------------------------------------------------")
    print("      bubbleSort   {}   {}   {}".format(timingAverages10[0],timingAverages100[0], timingAverages1000[0]))
    print("   selectionSort   {}   {}   {}".format(timingAverages10[2],timingAverages100[2], timingAverages1000[2]))
    print("   insertionSort   {}   {}   {}".format(timingAverages10[1],timingAverages100[1], timingAverages1000[1]))
    print("       shellSort   {}   {}   {}".format(timingAverages10[3],timingAverages100[3], timingAverages1000[3]))
    print("       mergeSort   {}   {}   {}".format(timingAverages10[4],timingAverages100[4], timingAverages1000[4]))
    print("       quickSort   {}   {}   {}".format(timingAverages10[5],timingAverages100[5], timingAverages1000[5]))
###############################################################################
def main():
    randomTesting(10)
    sortedTesting(10)
    shuffledTesting(10)
    almostTesting(10)
main()

