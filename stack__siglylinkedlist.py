class Node:
    def __init__(self,key):
        self.data=key
        self.next=None
        
class Stack__Singlylinked__list:
    def __init__(self):
        self.head=None
        self.n=0
        self.top=None
        
    def insert__ele(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.n+=1
            self.top=new_node
            return
        else:
            self.top.next=new_node
            self.top=new_node
            self.n+=1
            
    def remove__ele(self):
        if self.n==0:
            return
        if self.n==1:
            self.head=self.top=None
        else:
            n=self.head
            while n.next is not self.top:
                n=n.next
            x=self.top.data
            print("the removed data",x)
            n.next=None
            self.top=n
            
    def print__top(self):
        if self.n==0:
            return
        else:
            print(self.top.data)
            
    def print__stack(self):
        if self.n==0:
            return
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
            return
        
        
ob=Stack__Singlylinked__list()
ob.insert__ele(1)
ob.insert__ele(2)
ob.insert__ele(3)
ob.insert__ele(4)
ob.insert__ele(5)
ob.insert__ele(6)
ob.print__stack()
ob.remove__ele()
ob.print__top()
ob.print__stack()

            
            