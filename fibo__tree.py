class Fibo__Tree:
    def __init__(self,ele):
        self.insert__ele(ele)
        
    def insert__ele(self,ele):
        if ele<=1:
            self.data=ele
            self.lchild=None
            self.rchild=None
            
        else:
            self.data=ele
            self.lchild=Fibo__Tree(ele-1)
            self.rchild=Fibo__Tree(ele-2)
            
        return 
    
    def inorder(self):
        if self.data==None:
            return
        else:
            if self.lchild:
                self.lchild.inorder()
            print(self.data)
            if self.rchild:
                self.rchild.inorder()
    
ob=Fibo__Tree(2)
ob.inorder()




