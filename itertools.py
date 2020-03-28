import itertools
def fun(a):
    k=itertools.product('HT',repeat=a)
    s=list(k)
    output=["".join(temp) for temp in s]
    l=len(output)
    if a>2:
        for i in range(0,l):
            if "TTT" in output[i]:
                l=l-1
        print(l)
n=int(input("enter number of tosses"))        
fun(n)
