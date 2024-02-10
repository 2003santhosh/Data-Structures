
'''                
height, delete


'''


class Binary_tree_using_dict:
    def __init__(self):
        self.tree={}
        self.root=None
        
    def insert_ele(self,element):
        
        if len(self.tree)==0 and self.root==None:
            self.tree[element]=[None]*2
            self.root=element
            return
            
        if element in self.tree:
            return
        
        self.insert_ele1(element,self.root)
        
    def insert_ele1(self,element,present_node):
        
        if element<present_node:
            if self.tree[present_node][0]==None:
                self.tree[present_node][0]=element
            else:
                x=self.tree[present_node][0]
                self.insert_ele1(element,x)
                
        if element>present_node:
            if self.tree[present_node][1]==None:
                self.tree[present_node][1]=element
            else:
                x=self.tree[present_node][1]
                self.insert_ele1(element,x)
                
        self.tree[element]=[None]*2
        
        
    def print_tree(self):
        if len(self.tree)==0:
            return
        for i in self.tree:
            print(i,self.tree[i])
        
    def print_root(self):
        if len(self.tree)==0:
            return
        return self.root
        
    def inorder(self,present_node,lst=[]):
        if self.root==None:
            return
        if self.tree[present_node][0]!=None:
            x=self.tree[present_node][0]
            self.inorder(x,lst)
        lst.append(present_node)
        if self.tree[present_node][1]!=None:
            x=self.tree[present_node][1]
            self.inorder(x,lst)
        
        return lst
        
    def preorder(self,present_node,lst=[]):
        if self.root==None:
            return
        lst.append(present_node)
        if self.tree[present_node][0]!=None:
            x=self.tree[present_node][0]
            self.inorder(x,lst)
        if self.tree[present_node][1]!=None:
            x=self.tree[present_node][1]
            self.inorder(x,lst)

        return lst
            
    def postorder(self,present_node,lst=[]):
        if self.root==None:
            return
        
        if self.tree[present_node][0]!=None:
            x=self.tree[present_node][0]
            self.inorder(x,lst)
        if self.tree[present_node][1]!=None:
            x=self.tree[present_node][1]
            self.inorder(x,lst)
        lst.append(present_node)

        return lst
        
        
    def beadth_first_search(self):
        if self.root==None:
            return
        
        lst=[]
        queue=[self.root]
        while queue:
            x=queue.pop(0)
            lst.append(x)
            if self.tree[x][0]:
                queue.append(self.tree[x][0])
                
            if self.tree[x][1]:
                queue.append(self.tree[x][1])
                
        return lst
        
    def depth(self,present_node,depth=0):
        
        if self.has_parent(present_node)!=True:
            print(depth)
            return depth
        if self.root==None:
            return 0
            
        
        x=self.get_parent(present_node)
        depth+=1
        self.depth(x,depth)
            
        
            
    def has_parent(self,element):
        if self.root==None:
            return
        if element==self.root:
            return False
        for i in self.tree:
            for j in self.tree[i]:
                #print(j)
                if j is not None and j==element:
                    
                    return True
                    
                    
                    
    def get_parent(self,element):
        if self.root==None:
            return
        for i in self.tree:
            for j in self.tree[i]:
                if j is not None and j==element:
                    
                    return i
        
        
    
        
    
ob=Binary_tree_using_dict()
ob.insert_ele(100)
ob.insert_ele(90)
ob.insert_ele(110)
ob.insert_ele(10)
ob.print_tree()
x=ob.inorder(ob.root)
print(x)
x=ob.beadth_first_search()
print(x)
x=ob.depth(10)
print(x)



