d=[]
l=[]
a=int(raw_input())
for i in range(0,a):
    l.append(int(raw_input()))


l.sort(reverse=True)
for i in l:
    d.append(str(i))
b=int("".join(d))
print b
