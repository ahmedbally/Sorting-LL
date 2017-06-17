from random import randrange
from time import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data=data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size =0

    def isEmpty(self):
        return self.head is None

    def append(self, item):

        temp = Node(item)
        temp.next = self.head 
        if self.head is None:
            self.tail = temp
        self.head = temp
        self.size +=1

    def appendSort(self,temp):
        temp.next=None
        current=self.tail
        previous=None
        var=temp.data
        while current is not None:
            if current.data > var:
                break
            else:
                previous=current
                current=current.next
        if previous is None:
            temp.next=self.tail
            self.tail=temp
        else:
            temp.next=current
            previous.next=temp


    def lenght(self):
        current = self.head
        count=0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current=self.head
        previous = None
        found=False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if  previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size-=1



def insertionSortL(llist):         
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
      

List = []
LList = LinkedList()
LLList = LinkedList()
for i in range(10000):
    List.append(randrange(-1000,1001))
for i in List:
    LLList.append(i)


start_time=time()
s=insertionSortL(LLList)
end_time=time()
print("Linked list insertion time: ",end_time-start_time)

start_time = time()
insertionSort(List)
end_time = time()
print("Ordinary list insertion time: ",end_time-start_time)
