l=list(map(int,input().split(" ")))
l1=set(l)
l1.remove(max(l))
print(max(l1))


