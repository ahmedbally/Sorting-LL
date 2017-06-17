from LinkedList import *


def insertionSortL(llist):            #Short time
  for i in range(llist.size-1):
    temp=llist.head
    llist.head = temp.getNext()
    llist.appendSort(temp)
  return llist.tail

def insertionSort(alist):
    for index in range(1, len(alist)):
      currentvalue = alist[index]
      position = index

      while position > 0 and alist[position - 1] > currentvalue:
         alist[position] = alist[position - 1]
         position = position - 1
      alist[position] = currentvalue




