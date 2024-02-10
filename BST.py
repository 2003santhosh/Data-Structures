class Binarysearchtree:
    def __init__(self,key):
        self.key=key
        self.rchild=None
        self.lchild=None
       
    def insert__ele(self,ele):
        if self.key==ele:
            return
        if ele<self.key:
            if self.lchild:
                self.lchild.insert__ele(ele)
            else:
                self.lchild=Binarysearchtree(ele)
                
        else:
            if self.rchild:
                self.rchild.insert__ele(ele)
            else:
                self.rchild=Binarysearchtree(ele)
                
    def inorder(self,lst=[]):
        if self.key==None:
            return
        else:
            if self.lchild:
                self.lchild.inorder()
            lst.append(self.key)
            if self.rchild:
                self.rchild.inorder()
                
        return lst
                
    def preorder(self,lst=[]):
        if self.key==None:
            return 
        else:
            lst.append(self.key)
            if self.lchild:
                self.lchild.preorder()
            if self.rchild:
                self.rchild.preorder()
                
        return lst
                
    def postorder(self):
        if self.key==None:
            return
        else:
            if self.lchild:
                self.lchild.postorder()
            if self.rchild:
                self.rchild.postorder()
            print(self.key)
        
                
    def is__leaf(self,ele): # it is not generalized
        if self.lchild==None and self.rchild==None:
            
            return 1
        if ele<self.key:
            self.lchild.is__leaf(ele)
        if ele>self.key:
            self.rchild.is__leaf(ele)
        else:
            return
        
            
            
    def is__parent(self,ele):
        if self.key==None:
            return 0
        if self.lchild==None and self.rchild==None:
            print('it is  not')
            return 0
        if ele<self.key:
            if self.lchild:
                self.lchild.is__parent(ele)
                return
        if ele>self.key:
            if self.rchild:
                self.rchild.is__parent(ele)
                return
        else:
            print('yes it is a parent')
            return 1
            
    def print__all__leaf(self,lst=[]):
        if self.lchild==None and self.rchild==None:
            lst.append(self.key)
            
        if self.lchild:
            self.lchild.print__all__leaf(lst)
            
            
        if self.rchild:
            self.rchild.print__all__leaf(lst)
            
        return lst
        
    def print__children(self,ele):
        if self.key==ele:
            if self.lchild is not None:
                print(self.lchild.key)
            if self.rchild is not None:
                print(self.rchild.key)
        if ele<self.key:
            if self.lchild:
                self.lchild.print__children(ele)
            else:
                return
            
        else:
            if self.rchild:
                self.rchild.print__children(ele)
            else:
                return
            
    def print__parent(self,ele):
        if self.key==None:
            return
        if self.lchild!=None:
            
            if self.lchild.key==ele:
                print(self.key)
                
        if self.rchild!=None:
            
            if self.rchild.key==ele:
                print(self.key)
        
        if ele<self.key:
            if self.lchild:
                self.lchild.print__parent(ele)
                
            else:
                return
            
        if ele>self.key:
            if self.rchild:
                self.rchild.print__parent(ele)
                
            else:
                return
            
    
                
    def print__position(self,ele,t=0):
        if self.key==None:
            return
        if self.key==ele:
            print(t)
            return
        if ele<self.key:
            if self.lchild:
                self.lchild.print__position(ele,2*t+1)
            else:
                return
                
        else:
            if self.rchild:
                self.rchild.print__position(ele,2*t+2)
            else:
                return
            
    def is__root(self,ele):
        return self.key==ele
                
    def is__empty(self):
        return self.key==None
        
    def num__children(self,ele):
        if self.key==None:
            return
        
        if self.key==ele:
            sum=0
            if self.lchild:
                sum+=1
            if self.rchild:
                sum+=1
            print(sum)
            return
            
        if ele<self.key:
            if self.lchild:
                self.lchild.num__children(ele)
            else:
                return
        
        if ele>self.key:
            if self.rchild:
                self.rchild.num__children(ele)
            else:
                return
            
    def depth(self,ele,d=0):
        if self.key==None:
            return
        
        if self.key==ele:
            return d
            
        if ele<self.key:
            if self.lchild:
                self.lchild.depth(ele,d+1)
            else:
                return
            
        if ele>self.key:
            if self.rchild:
                self.rchild.depth(ele,d+1)
            else:
                return
  


    def parent_ele(self,ele):
        if self.key==None:
            return
        if ele<self.key:
            if self.lchild:
                if self.lchild.key==ele:
                    return 1
                else:
                    self.lchild.parent_ele(ele)
            else:
                return 0

        if ele>self.key:
            if self.rchild:
                if self.rchild.key==ele:
                    return 1
                else:
                    self.rchild.parent_ele(ele)
                    
            else:
                return 0

        return 0
        
    def ancestors(self,ele,lst):
        if self.key==None:
            return
        if self.key==ele:
            #print(lst)
            return lst
            
        if ele<self.key:
            if self.lchild:
                lst.append(self.key)
                self.lchild.ancestors(ele,lst)
            else:
                return
            
        if ele>self.key:
            if self.rchild:
                lst.append(self.key)
                self.rchild.ancestors(ele,lst)
            else:
                return
            
    def find_first_common_ancestors(self,ele1,ele2):
        lst1=self.ancestors(ele1,[])
        lst2=self.ancestors(ele2,[])
        if not lst1 or not lst2:
            return 
        lst1.reverse()
        lst2.reverse()
        for i in lst1:
            if i in lst2:
                print(i)
                return i
                
                
    def top_view(self): # the answer wrong
        if self.key==None:
            return
        lst=[self.key]
        lst1=self.top_view_left_side([])
        lst2=self.top_view_right_side([])
        lst1+=lst+lst2
        print(lst1)
            
    def top_view_left_side(self,lst=[]):
        if self.lchild:
            lst.append(self.lchild.key)
            self.lchild.top_view_left_side(lst)
            
        #print(lst)
        return lst
        
        
    def top_view_right_side(self,lst=[]):
        if self.rchild:
            lst.append(self.rchild.key)
            self.rchild.top_view_right_side(lst)
            
        #print(lst)
        return lst
        

    
                
                
    
            
        
ob=Binarysearchtree(90)
ob.insert__ele(20)
ob.insert__ele(30)
ob.insert__ele(90)
ob.insert__ele(100)
#ob.is__parent(20)
#x=ob.print__all__leaf()
#print(x)
#x=ob.preorder()
#print(x)

#print()
#ob.print__sibling(20)
#ob.print__position(0)
#ob.depth(100)
#ob.height()
#ob.top_view()
ob.breadth_first_search()


