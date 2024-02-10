class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Doubly__linked__list:
    def __init__(self):
        self.n=0
        self.head=None
        self.tail=None
        
    def insert__ele__front(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.tail=new_node
            self.n+=1
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.n+=1
        return
    
    def insert__ele__last(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.tail=new_node
            self.n+=1
            return
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.n+=1
            return
        
    def print__list(self):
        if self.n==0:
            return
        
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
                
            return
        
    def print__head(self):
        if self.n==0:
            return
        else:
            print(self.head.data)
            
    def print__tail(self):
        if self.n==0:
            return
        else:
            print(self.tail.data)
            
    def delete__front(self):
        if self.n==0:
            return
        if self.n==1:
            self.n-=1
            self.head=self.tail=None
            return
        else:
            self.head=self.head.next
            self.head.prev=None
            self.n-=1
            return
        
    def delete__last(self):
        if self.n==0:
            return
        if self.n==1:
            self.head=self.tail=None
            self.n-=1
            return
        else:
            self.tail.prev=self.tail
            self.tail.next=None
            self.n-=1
            return
            
        
ob=Doubly__linked__list()
ob.insert__ele__front(2)
ob.insert__ele__front(3)
ob.insert__ele__last(1)
ob.insert__ele__front(4)
ob.delete__last()
ob.print__tail()
print()

ob.print__list()





