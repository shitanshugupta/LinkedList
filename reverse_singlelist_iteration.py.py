class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next 

class LinkedList:
    def __init__(self):
        self.head=None
    #insert at beginning
    def insert_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def reverse_list(self):
        self.pre=None
        self.current=self.head
        self.nextnode=self.head
        while self.current is not None:
            self.nextnode=self.current.next
            self.current.next=self.pre
            self.pre=self.current
            self.current=self.nextnode
        self.head=self.pre

    def display(self):
        temp=self.head
        st=" "
        while temp is not None:
            suffix=" "
            if temp.next:
                suffix="--->"
            st+=str(temp.data)+suffix
            temp=temp.next
        print(st)
root=LinkedList()
root.insert_beginning(10)
root.insert_beginning(55)
root.insert_beginning(7)
root.insert_beginning(25)
root.insert_beginning(40)
root.insert_beginning(98)
root.display()
root.reverse_list()
root.display()

