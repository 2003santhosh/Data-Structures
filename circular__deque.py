class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
        
        
class Circular__deque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.n=0
        
    def insert__front(self,ele):
        #print("hi")
        new_node=Node(ele)
        if self.n==0:
            #print("hi")

            self.head=new_node
            self.tail=new_node
            self.tail.next=new_node
            new_node.next=self.tail
            self.n+=1
            return
        else:
            #print("hi")

            new_node.next=self.tail.next
            self.tail.next=new_node
            self.head=new_node
            self.n+=1
            return
        
    def insert__behind(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.tail=new_node
            self.tail.next=new_node
            new_node.next=self.tail
            self.n+=1
            return
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
            self.n+=1
            return
        
    def remove__front(self):
        if self.n==0:
            return
        
        if self.n==1:
            x=self.head
            print("the removed element" , x.data)
            self.head=self.tail=None
            self.n-=1
            return
            
        else:
            x=self.head
            print("the removed element" , x.data)
            self.tail.next=self.head.next
            self.n-=1
            self.head=self.tail.next
            return
        
    def remove__behind(self):
        if self.n==0:
            return
        
        if self.n==1:
            x=self.head
            print("the removed element" , x.data)
            self.head=self.tail=None
            self.n-=1
            return
        
        else:
            n=self.head
            while n.next is not self.tail:
                n=n.next
                
            x=self.tail
            print(x.data)
            n.next=self.head
            self.tail=n
            self.n-=1
            return
        
    def print__head(self):
        if self.n==0:
            print("the list is empty")
            return
        else:
            print(self.head.data)
            return
        
    def print__tail(self):
        if self.n==0:
            print("the list is empty")
            return
        else:
            print(self.tail.data)
            return
        
    def print__list(self):
        if self.n==0:
            print(1)
            return
        else:
            n=self.head
            #print(1)
            while n.next is not self.head:
                #print(1)
                print(n.data)
                n=n.next
            print(self.tail.data)
                
            return
        
ob=Circular__deque()
ob.insert__front(1)
ob.insert__front(2)
ob.insert__front(3)
ob.insert__front(4)
ob.insert__front(5)
ob.print__list()
ob.insert__behind(12)
ob.remove__behind()
print()
ob.print__head()
ob.print__tail()


            
        
            
        
        
        
        
        
        
            
            


