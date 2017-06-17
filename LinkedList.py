from Node import *
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
