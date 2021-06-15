class Node:
    def __init__(self,data=None,pre=None,next=None):
        self.data=data
        self.prev=pre
        self.next=next

class DoublyList:
    def __init__(self):
        self.head=None

    #insert at beginning
    def insert_beginning(self,data):
        node=Node(data,None,self.head)
        self.head=node
    
    #insert at the end
    def insert_end(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        node=Node(data)
        temp.next=node
        node.pre=temp
        return

    #insert at the position
    def insert_position(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.insert_end()
            return
        i=0
        temp=self.head
        while i<=index-2:
            temp=temp.next
            i+=1
        node=Node(data)
        node.next=temp.next
        temp.next=node
        node.pre=temp
        temp.next.pre=node
    
    def del_beginning(self):
        self.head=self.head.next 
        self.head.pre=None
        return  

    def del_end(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None

    def del_position(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.del_beginning()
        i=0
        temp=self.head
        while i<=index-2:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        temp.next.next.pre=temp
        
    #display the nodes
    def display(self):
        temp=self.head
        st=""
        while temp is not None:
            suffix=""
            if temp.next:
                suffix="-->" "<--"
            st+=str(temp.data)+suffix
            temp=temp.next
        print(st)

    #total number of nodes
    def get_length(self):
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
root=DoublyList()
root.insert_beginning(10)
root.insert_beginning(20)
root.insert_beginning(55)
root.insert_end(100)
root.insert_end(200)
root.insert_beginning(11)
root.insert_position(2,555)
root.del_beginning()
root.del_position(2)
root.del_end()
root.display()
cnt=root.get_length()
print(f"total number of nodes in doubly list is {cnt}")    