flag=0
l=[]
c=[]
d={}
j=0
a=int(input())
for i in range(0,a):
    l.append(input())
set1=set(l)
b=set1.pop()
l.remove(b)
b=list(b)
print(b)
print(l)
while(j<len(b)):
    if flag==-1:
        break
    for i in l:
        if b[j]==i[j]:
            flag=0
        else:
            flag=-1
            break
    if flag==0:
        c.append(b[j])
    j=j+1
c="".join(c)
print (c)
   
    