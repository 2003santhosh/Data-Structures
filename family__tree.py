# tree with 3 children

class Tree__3__children:
    def __init__(self,c):
        self.c=c
        self.n=0
        self.data=[None]*c
        
    def parent__idx(self,x):
        return ((x-1)//3)
        
    def _1st__child__idx(self,x):
        return (3*x+1)
        
    def _2nd__child__idx(self,x):
        return (3*x+2)
        
    def _3rd__child__idx(self,x):
        return (3*x+3)
        
    def print__treee(self):
        print(self.data)
        
    def parent__value(self,x):
        if self.n==0:
            return
        if self.parent__idx(x)>=0:
            return self.data[self.parent__idx(x)]
            
    def _1st__child__value(self,x):
        if self.data[self._1st__child__idx(x)]!=None:
            return self.data[self._1st__child__idx(x)]
            
    def _2nd__child__value(self,x):
        if self.data[self._2nd__child__idx(x)]!=None:
            return self.data[self._2nd__child__idx(x)]
            
    def _3rd__child__value(self,x):
        if self.data[self._3rd__child__idx(x)]!=None:
            return self.data[self._3rd__child__value(x)]
            
            
    def insert(self,ele):
        if ele in self.data:
            return
        if self.n==self.c:
            self.resize(self.c)
        
        self.data[self.n]=ele
        self.n+=1
        return
        
    def print__Tree(self):
        print(self.data)
        
    def resize(self,c):
        x=[None]*(2*c)
        for i in range(self.n):
            x[i]=self.data[i]
            
        self.data=x
        self.c=2*c
        
        
ob=Tree__3__children(10)
ob.insert(10)
ob.insert(9)
ob.insert(8)
ob.insert(7)
ob.insert(6)
ob.insert(5)
ob.insert(4)
ob.print__Tree()

            
        
            
            
            
            
            
            
            