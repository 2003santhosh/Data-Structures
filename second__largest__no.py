def find__max(lst):
    if len(lst)==0:
        return
    else:
        max=lst[0]
        for i in range(len(lst)):
            if max<lst[i]:
                max=lst[i]
                
                
        return max
        
        
def diff__lst(lst,max):
    emp__lst=[]
    for i in range(len(lst)):
        diff=max-lst[i]
        emp__lst.append(diff)
        
    return emp__lst

def find__2__largest(lst):
    if lst[0]==0:
        x=1
        min__diff=lst[1]
        for i in range(1,len(lst)):
            if min__diff>lst[i]:
                min__diff=lst[i]
                x=i
        return x
    
    min__diff=lst[0]
    x=0
    #print(min__diff)
    for i in range(len(lst)):
        if lst[i]==0:
            continue
        else:
            if min__diff>lst[i]:
                min__diff=lst[i]
                x=i
    
    return x
    
    
    
lst=[1001,2,3,4,5,6,7,8,89,76,543,234,235,34]
x=find__max(lst)
y=diff__lst(lst,x)
#print(y)
z=find__2__largest(y)     
print(lst[z])
        
        
        
        
        
        
        
        
        
        
        
            
            
