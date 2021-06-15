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
    # insert at the end
    def insert_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        node=Node(data)
        temp.next=node
        
    # insert at some position
    def insert_position(self,index,data):
        if index < 0 or index >self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.insert_beginning(data)
            return
        i=0
        temp=self.head
        while i<=index-2:
            temp=temp.next
            i+=1
        node=Node(data,temp.next)
        temp.next=node

    # inserting multiple at a time in linked list
    def insert_multiple(self,lst):
        for i in lst:
            self.insert_end(i)



    # deletion at beginning
    def del_beginning(self):
       self.head=self.head.next

    # deletion at end
    def del_end(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None 
    #deletion at position
    def del_position(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")

        elif index==0:
            self.del_beginning()
            return
        elif index==self.get_length:
            self.del_end()
            return
        else:
            temp=self.head
            i=0
            while i<=index-2:
                temp=temp.next
                i+=1
            temp.next=temp.next.next
            
         
    def display(self):
        temp=self.head
        st=" "
        while temp is not None:
            suffix=" "
            if temp.next:
                suffix="-->"
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

if __name__=="__main__":
    root=LinkedList()
    lst=["apple","banana","mango","orange"]
    root.insert_multiple(lst)
    root.insert_beginning(1)
    root.insert_beginning(5)
    root.insert_beginning(10)
    root.insert_end(200)
    root.insert_end(199)
    root.insert_position(2,55)
    root.insert_position(0,155)
    root.insert_position(1,1000)
    root.display()
    root.del_beginning()
    root.del_end()
    root.del_position(2)
    root.display()
    le=root.get_length()
    print(f"Total number of nodes in the linked list is {le} ")











