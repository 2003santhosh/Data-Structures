class Tree__array:
    def __init__(self,c):
        self.c=c
        self.n=0
        self.data=[None]*c
        
    def parent__idx(self,x):
        return ((x-1)//2)
        
    def lchild__idx(self,x):
        return (2*x+1)
        
    def rchild__idx(self,x):
        return (2*x+2)
        
    def parent__value(self,x):
        if self.n==0:
            return
        if self.parent__idx(x)>=0:
            return self.data[self.parent__idx(x)]
            
    def lchild__value(self,x):
        if self.data[self.lchild__idx(x)]!=None:
            return self.data[self.lchild__idx(x)]
            
    def rchild__value(self,x):
        if self.data[self.rchild__idx(x)]!=None:
            return self.data[self.rchild__idx(x)]
            
    def insert__ele(self,ele,i=0):
        if self.n==0:
            self.data[0]=ele
            self.n+=1
            return
        if ele<self.data[i]:
            if self.lchild__value(i):
                self.insert__ele(ele,(2*i+1))
            else:
                self.data[2*i+1]=ele
                
        if ele>self.data[i]:
            if self.rchild__value(i):
                self.insert__ele(ele,(2*i+2))
            else:
                self.data[2*i+2]=ele
                
                
    def print__tree(self):
        print(self.data)
        
    def preorder(self,i=0):
        if self.n==0:
            return
        else:
            print(self.data[i])
            if self.lchild__value(i):
                self.preorder(2*i+1)
            if self.rchild__value(i):
                self.preorder(2*i+2)
                
    def postorder(self,i=0):
        if self.n==0:
            return
        else:
            if self.lchild__value(i):
                self.preorder(2*i+1)
            if self.rchild__value(i):
                self.preorder(2*i+2)
            print(self.data[i])
            
            
    def inorder(self,i=0):
        if self.n==0:
            return
        else:
            if self.lchild__value(i):
                self.preorder(2*i+1)
            print(self.data[i])
            if self.rchild__value(i):
                self.preorder(2*i+2)
                
    '''def levelorder__level__wise(self,l,i=0): # this is a bit challenging as we have to traverse to that level (may be preorder concept can be used to print the elements)
        if self.n==0:
            return
        else:
            if l==0:
                print(self.data[0])
                return
            if '''
            
            
    def levelorder(self):
        if self.n==0:
            return
        for i in self.data:
            if i:
                print(i)
                
    def is__leaf(self,x):
        sum=0
        #idx1=self.lchild__idx(x)
        #idx2=self.rchild__idx(x)
        if self.lchild__value(x):
            sum+=1
        if self.rchild__value(x):
            sum+=1
        if self.data[x]==None:
            return
        if sum==0:
            return 1
        else:
            return
            
    def is__parent(self,x):
        sum=0
        #idx1=self.lchild__idx(x)
        #idx2=self.rchild__idx(x)
        if self.lchild__value(x):
            sum+=1
        if self.rchild__value(x):
            sum+=1
        if self.data[x]==None:
            return 
        if sum>0:
            return 1
        else:
            return 
        
    def value__to__idx(self,ele,i=0): # working properly , but the problem is when we are calling the method outside the class it is returning the value of index and None also
        if self.n==0:
            return 
        else:
            if self.data[i]==ele:
            
                return i
                
            if ele<self.data[i]:
                if self.lchild__value(i):
                    self.value__to__idx(ele,(2*i+1))
                else:
                    return 
            if ele>self.data[i]:
                if self.rchild__value(i):
                    self.value__to__idx(ele,(2*i+2))
                else:
                    return 
                    
                
            
    def depth(self,i,sum=0): # it is wroking properly but while returning the value of sum we are getting the depth value and None , the same problem faced in the method value__to__idx
        if self.parent__value(i):
            #print('Hi')
            self.depth((i-1)//2,sum+1)
        else:
            print(sum)
            
    
            
            
    def print__sibling(self,x):
        if self.n==0:
            return
        if x==0:
            return
        else:
            x1=self.parent__idx(x)
            x2=self.lchild__idx(x1)
            x3=self.rchild__idx(x1)
            if x2==x:
                print(self.data[x3])
            else:
                print(self.data[x2])
                
    
        
    def get__ancestor(self,x):
        if self.n==0:
            return
        else:
            x1=self.parent__idx(x)
            if self.parent__value(x1):
                return self.parent__idx(x1)
            else:
                return
    
    def get__descendent(self,x):
        if self.n==0:
            return
        else:
            lst=[(4*x+i) for i in range(3,7)] # we are getting this 4x + i by calculating the formula 
            for i in lst:
                if self.data[i]:
                    print(self.data[i])
                    
    
        
    def left__view(self,i=0):
        if self.n==0:
            return
        else:
            if self.data[i]!=None:
                print(self.data[i])
                return self.left__view(2*i+1)
                
    def right__view(self,i=0):
        if self.n==0:
            return
        else:
            if self.data[i]!=None:
                print(self.data[i])
                return self.right__view(2*i+2)
                
            
            
            
        
            
            
    
    
            
            
            
            
            
            
                
                
                
            
        

        
ob=Tree__array(20)
ob.print__tree()
ob.insert__ele(100)
ob.insert__ele(90)
ob.insert__ele(80)
ob.insert__ele(110)
ob.insert__ele(120)
ob.print__tree()
#x=ob.height(1)
#print(x)
#ob.deletion(80)
#x=ob.value__to__idx(120)
#print(x)
ob.right__view()
#print(x)
            
            
            
            
            