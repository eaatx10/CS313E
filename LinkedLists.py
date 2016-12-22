#  File: LinkedLists.py
#  Description: This program has methods that serves to both kinds of Linked Lists.
#  Student's Name: Elias Ansari
#  Student's UT EID: eaa957
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 4/6/16
#  Date Last Modified: 4/8/16
#############################################################################
class Node (object):
  def __init__ (self, item):
      self.item = item
      self.next = None

  def __str__ (self):
      return str(self.item)

  def getData (self):
      return (self.item)

  def setData (self, item):
      self.item = item

  def getNext (self):
      return (self.next)

  def setNext (self, newNext):
      self.next = newNext

class LinkedList (object):
  def __init__(self):
      self.head = None
################################################################################
  def getLength (self):
     # Return the number of items in the list
     counter = 0
     current = self.head

     while current != None:
         counter += 1
         current = current.getNext()
     return counter
############################################################################### 
  def addFirst (self, item): 
     # Add an item to the beginning of the list
     newNode = Node(item)
     newNode.setNext(self.head)
     self.head = newNode
################################################################################
  def addLast (self, item): 
     # Add an item to the end of a list
     newNode = Node(item)
     current = self.head
     if current == None:
         self.head = newNode 
     else:
         while current.getNext() != None:
             current = current.getNext()
         current.setNext(newNode)
###############################################################################
  def addInOrder (self, item): 
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.
     newNode = Node(item)
     current = self.head
     prev = None
     stop = False

     while current != None and not stop:
         if current.getData() > item:
             stop = True
         else:
             prev = current
             current = current.getNext()

     if prev == None:
         newNode.setNext(self.head)
         self.head = newNode
     else:
         prev.setNext(newNode)
         newNode.setNext(current)
            
################################################################################
  def findUnordered (self, item): 
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     current = self.head
     found = False
     while current != None and not found:
         if current.getData() == item:
             found = True
         else:
             current = current.getNext()
     return found
################################################################################
  def findOrdered (self, item): 
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list.
     current = self.head
     found = False
     stop = False

     while current != None and not found and not stop:
         if current.getData() == item:
             found = True
         elif current.getData() > item:
             stop = True
         else:
             current = current.getNext()
     return found
###############################################################################     
  def delete (self, item):
     # Delete an item from an unordered list
     #    if found, remove the item from the list and 
     #    return True; otherwise, return False.
     current = self.head
     prev = None
     if current == None:
         return None
     else:
         while current.item != item:
             if current.next == None:
                 return None
             else:
                 prev = current
                 current = current.next
         if current == self.head:
             self.head = self.head.next
         else:
             prev.next = current.next
         return current
###############################################################################    
  def __str__ (self):
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements
     string = "  "
     current = self.head
     counter = 0
     while current != None:
         if counter < 10:
             string += current.getData() + "  "
             current = current.getNext()
             counter += 1
         else:
             string += "\n  " + current.getData() + "  "
             current = current.getNext()
             counter = 1
     return string
###############################################################################
  def copyList (self):
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements.  Do not
     #    change the original list.
     current = self.head
     newList = LinkedList()
     while current != None:
         item = current.getData()
         newList.addLast(item)
         current = current.getNext()
     return newList
###############################################################################
  def sortList (self,direction): 
     # Take a linked list and return the same list with elements
     #    sorted.  If direction is "I", then the list should
     #    be sorted in increasing order;  if direction is "D",
     #    then it should be decreasing order.
     # Do NOT use a sort function:  do this by iteratively
     #    traversing the list, removing elements, and then 
     #    inserting each item into the correct place in the
     #    updated list.
     list2 = LinkedList()
     current = self.head
     while current != None:
         item = current.getData()
         list2.addInOrder(item)
         current = current.getNext()
     self.head = list2.head

     if direction == "D":
         list3 = LinkedList()
         current = list2.head
         while current != None:
             item = current.getData()
             list3.addFirst(item)
             current = current.getNext()
         self.head = list3.head
     return self
##############################################################################     
  def isSorted (self):
     # Return True if a list is sorted in ascending (alphabetical)
     #    order, or False otherwise
     prev = self.head
     current = self.head.next
     while current.next != None:
         if current.item > prev.item:
             prev = current
             current = current.next
         else:
             return False
     return True
##############################################################################
  def isEmpty (self): 
     # Return True if a list is empty, or False otherwise
     return self.head == None
##############################################################################
  def mergeList (self, b): 
     # Return a new ordered list whose elements consist of the 
     #    elements of two ordered lists combined.  The original
     #    two lists should not be changed.
     current = self.head
     newList = LinkedList()
     while current != None:
         newList.addInOrder(current.getData())
         current = current.getNext()
     current = b.head
     while current != None:
         newList.addInOrder(current.getData())
         current = current.getNext()
     return newList
###############################################################################     
  def compareList (self,c):
     # Given two lists, return a new ordered list whose elements
     #    consist of items that appear in both of the two given
     #    lists.  The original two lists should not be changed.
     current = self.head
     newList = LinkedList()
     while current != None:
         currentC = c.head
         match = False
         while currentC != None and not match:
             if current.getData() == currentC.getData():
                 newList.addInOrder(current.getData())
                 match = True
             currentC = currentC.getNext()
         current = current.getNext()
     return newList
                 
##############################################################################
  def isEqual (self, b):
     # Test if two lists are equal, item by item, and return True.
     if self.getLength() != b.getLength():
         return False
     else:
         curr1 = self.head
         curr2 = b.head
         while curr1 != None:
             if curr1.getData() == curr2.getData():
                 curr1 = curr1.getNext()
                 curr2 = curr2.getNext()
             else:
                 return False
     return True
##############################################################################
  def removeDuplicates (self):
     # Modify a list, keeping only the first occurrence of an element
     #    and removing all duplicates.  Do not change the order of
     #    the remaining elements.
     list1 = LinkedList()
     current = self.head
     while current != None:
         if not list1.findUnordered(current.getData()):
             list1.addLast(current.getData())
         current = current.getNext()
     self.head = list1.head
     return self
################################################################################
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of sortList")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto!")
   
   print ("   Original list:")
   print (planets)
   print ("   List sorted into increasing order:")
   planets.sortList("I")
   print (planets)
   print ("   List sorted into decreasing order:")
   planets.sortList("D")
   print (planets)

   print ("\n\n***************************************************************")
   print ("Test of isSorted:  should see False, True")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto!")
   print ("   Original list:")
   print (planets)
   print ("   Should be False --> ", planets.isSorted())
   planets.sortList("I")
   print ("   After sort:")
   print (planets)
   print ("   Should be True --> ", planets.isSorted())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of compareList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("Parker")
   list1.addLast("Stark")
   list1.addLast("Grimm")
   list1.addLast("Storm")
   list1.addLast("Richards")
   list1.addLast("Rogers")
   list1.addLast("Pym")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("Rogers")
   list2.addLast("Summers")
   list2.addLast("Grey")
   list2.addLast("Stark")
   list2.addLast("Drake")
   list2.addLast("McCoy")
   list2.addLast("Worthington")
   print ("   second list:")
   print (list2)
   print ("   common items:")
   list3 = list1.compareList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()

