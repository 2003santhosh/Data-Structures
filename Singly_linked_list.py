class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None

class Singly_linked_list:
    def __init__(self):
        self.head=None
        self.n=0

    def insert_ele(self,ele):
        new_node=Node(ele)
        if self.head==None:
            self.head=new_node
            self.n+=1
            return

        n=self.head
        while n.next is not None:
            n=n.next

        n.next=new_node
        self.n+=1
        return

        
        
    def print__list(self):
        if self.head==None:
            return
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
                
            return
        
    def print__only(self):
        if self.head==None:
            return
        else:
            lst=[]
            n=self.head
            while n.next is not None:
                if n.data not in lst:
                    lst.append(n.data)
                n=n.next
                
            return lst
            
    def delete__ele(self,ele):
        if self.n==0:
            return
        if self.head.data==ele:
            self.head=self.head.next
            self.n-=1
            return
    
        else:
            n=self.head
            while n.next is not None:
                if n.next.data==ele:
                    break
                n=n.next
                
            else:
                return
                
            if n.next.next is None:
                n.next=None
                self.n-=1
                return
            
            else:
                n.next=n.next.next
                self.n-=1
                return
            
    def insert__sort(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.n+=1
            return
        
        if self.n==1:
            if self.head.data>ele:
                new_node.next=self.head
                self.head=new_node
                self.n+=1
                return
            
            else:
                self.head.next=new_node
                self.n+=1
                return
        
        
        else:
            if ele<self.head.data:
                new_node.next=self.head
                self.head=new_node
                self.n+=1
                return
            n=self.head
            while n.next is not None:
                if n.data<ele and n.next.data>ele:
                    break
                    
                    
                n=n.next
            
            
                
            new_node.next=n.next
            n.next=new_node
            self.n+=1
            return
        
      
    '''def sort__ele(self,x=self.head,t=0):
        if t==self.n:
            return
        if self.n==0:
            return
        else:
            # find the max and insert it in the front
            max=x.data
            n=x
            while n.next is not None:
                if max<n.data:
                    max=n.data
                    
                n=n.next
                
            self.delete__ele(max)
            self.insert__back(max)
            self.sort__ele(x.next,t+1)'''
            
    def insert__back(self,ele):
        new_node=Node(ele)
        if self.n==0:
            return
        else:
            new_node.next=self.head
            self.head=new_node
            self.n+=1
            return
            
    def check_first_sum(self):
        #if t==self.n:
            #return sum
        if self.n==0:
            return
        else:
            n=self.head
            sum=self.head.data
            while n.next is not None:
                if sum==n.next.data:
                    print(sum)
                   
                    
                else:
                    sum+=n.next.data
                    
                n=n.next
                    
            else:
                return 0
                
    def modular__idx(self,k):
        num=0
        if self.n==0:
            return
        else:
            n=self.head
            while n.next is not None:
                if n.data%k==0:
                    num=n.data
                n=n.next
                
            if num==0:
                return -1
            else:
                return num
                
                
    def insert__bw(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.n=1
            return
        r=(self.n+1)//2
        
        i=2
        n=self.head
        while i<=r:
            n=n.next
            i+=1
            
        new_node.next=n.next
        n.next=new_node
        self.n+=1
        return


    def reverse__lst(self):
        if self.n==0:
            return
        else:
            prev=None
            n=self.head
            while n is not None:
                next=n.next
                n.next=prev
                prev=n
                n=next
                
            self.head=prev
            
                
                
                
                
            
                
            
                
    def insert__front(self,ele):
        new_node=Node(ele)
        if self.n==0:
            self.head=new_node
            self.n+=1
            return
        else:
            new_node.next=self.head
            self.head=new_node
            self.n+=1
            return


    def delete__dup(self):
        if self.head==None:
            return
        
        n=self.head
        lst=[n.data]
        while n.next is not None:
            if n.next.data not in lst:
                lst.append(n.next.data)
                
            else:
                x=n.next
                y=x.next
                n.next=y
                self.n-=1
                continue
                
            n=n.next
        
    

                
            
    
            
ob=Singly_linked_list()
ob.insert__ele(1)
ob.insert__ele(2)
ob.insert__ele(3)
ob.insert__ele(4)
ob.insert__ele(5)

#ob.insert__bw(7)
ob.print__list()
#ob.reverse__lst()
print()
#ob.in__bw__in__bw()

                       
         