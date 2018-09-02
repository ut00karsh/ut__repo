import math
def cal(i1,l):
    for i in range(len(l)):
        for j in range(len(l)-i+1):
            count=0
            sum=0
            for k in range(j,j+i+1):
                sum+=l[k]*int(math.pow(10,count))
                count+=1
            print(sum)
            if(sum & i1==0):
                return "YES"
            
                
    return "NO"
            
l=[]
n=int(input())
for i in range(0,n):
    i1,i2=[int(x) for x in input().split(" ")]
    l=[int(x) for x in input().split(" ")]
    print(cal(i1,l))
    
    