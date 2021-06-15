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
    def reverse_list(self,temp):
        global count
        count=0
        if temp==None:
            return
        
        self.reverse_list(temp.next)
        count+=1
        if count ==self.get_length():
            print(temp.data,end=" ")
        else:
            print(f"{temp.data}{'--->'}",end="")

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

    def get_length(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        return count


root=LinkedList()
root.insert_beginning(10)
root.insert_beginning(55)
root.insert_beginning(7)
root.insert_beginning(25)
root.insert_beginning(40)
root.insert_beginning(98)
root.display()
root.reverse_list(root.head)

