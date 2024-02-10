class Deque:
    def __init__(self):
        self.data=[]
        self.n=0
        self.head=None
        self.tail=None
        
    def insert__last(self,ele):
        
        #print("hi")
        self.data.append(ele)
        self.n+=1
        self.tail=ele
        self.head=self.data[0]
        
    def remove__last(self):
        if self.n==0:
            return
        else:
            x=self.data.pop()
            self.n-=1
            self.tail=self.data[-1]
            return x
        
    def insert__front(self,ele):
        self.data.insert(0,ele)
        self.head=ele
        self.tail=self.data[-1]

        self.n+=1
        return
    
    def remove__front(self):
        if self.n==0:
            return
        else:
            x=self.data.pop(0)
            self.n-=1
            return x
            
    def print__list(self):
        print(self.data)
        
    def print__head(self):
        print(self.head)
        
    def print__tail(self):
        print(self.tail)
        
        
        
        
ob=Deque()

ob.insert__last(1)     
ob.insert__front(2)     
ob.insert__last(3)     
ob.insert__last(4)     
ob.remove__front()    
ob.insert__last(6)
ob.insert__last(10)

ob.remove__last()
ob.print__head()
ob.print__tail()
ob.print__list()

    
        


