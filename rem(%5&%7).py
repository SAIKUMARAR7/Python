l=[12,24,35,70,88,120,155]
for i in l:
    if(i%5==0)and(i%7==0):
        l1=[i]
for i in l:
    if i in l1:
        l.remove(i)
print(l)
