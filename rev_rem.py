a=input()
b=['a','e','i','o','u']
l=list(a)
for i in l:
    if i in b:
        l.remove(i)
l=(l[::-1])
l="".join(l)
print(l)