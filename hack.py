import math	
def cal(i1,l):
	for i in range(len(l)):
		for j in range(len(l)-i):
			s=""
			for k in range(j,j+i+1):
				s=s+str(l[k])
			if(int(s)&i1 == 0):
				return "yes" 
			
	return "NO"
l=[]
n=int(input())
for i in range(0,n):
	i1,i2=[int(x) for x in input().split(" ")]
	l=[int(x) for x in input().split(" ")]
	print(cal(i1,l))
    
    
