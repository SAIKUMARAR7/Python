x,y=(map(int,input().split(" ")))
s=0
l=[]
for i in range(x,y+1):
    for j in str(i):
        print(j)
        if j=='1' or j=='4'or j=='9':
            s=s+1
    if(s==len(str(i))):
        l.append(i)
        s=0
    s=0
print(l)
