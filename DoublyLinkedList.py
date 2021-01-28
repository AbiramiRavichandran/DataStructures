class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + " --> "
            itr = itr.next


        print(lstr)


    def addAtBegining(self,data):
        node = Node(data,None,self.head)
        self.head = node

    def addAtEnd(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next =  Node(data,itr,None)


    def delByValue(self,data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev =  None
            return

        itr = self.head.next

        while itr:
            if itr.data == data:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                break
            itr = itr.next


    ll = LinkedList()
    ll.print()
    ll.addAtBegining(2)
    ll.addAtBegining(5)
    ll.print()
    ll.addAtEnd(4)
    ll.print()
