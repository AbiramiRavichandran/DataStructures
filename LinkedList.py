class Node:
    def __init__(self,data=none,next=none):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return

        itr = self.head
        str = ""
        while itr.next != None:
            str += str(itr.data) + " --> "
            itr = itr.next
        print(str)


    def addAtBegining(self,data):
        node = Node(data,self.head)
        self.head = node

    def addAtEnd(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr =  Node(data,None)

    def delByValue(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next






ll = LinkedList()
ll.print()
ll.addAtBegining(2)
ll.addAtBegining(5)
ll.print()
ll.addAtEnd(4)
ll.print()
