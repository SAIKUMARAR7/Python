class node:
    def __init__(self,x):
        self.data=x
        self.add=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        newnode=node(data)
        newnode.add=self.head
        self.head=newnode
    def insert_end(self,a):
        newnode=node(a)
        last=self.head
        while(last.add):
            last=last.add
        last.next=newnode
    def insert_mid(self,previous,d):
        if previous.add==None:
            print("node not exists")
            return
        new_node=node(d)
        newnode.add=previous.add
        previous.add=newnode
    def del_beg(self):
        temp=self.head
        self.head=self.head.add
        temp.add=None
    def delete(self,k):
        temp=self.head
        if(temp is not none):
            if(temp.data==k):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data==key:
                break
            pre=temp
            temp=temp.add
        if(temp==none):
            return
        pre.add=temp.add
        temp=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,"==>",end=' ')
            temp=temp.add

l1=linkedlist()
l1.head=node(100)
n1=node(200)
n2=node(300)
n3=node(400)

l1.head.add=n1
n1.add=n2
n2.add=n3
print("1.insert_beg","2.insert_end","3.insert_mid","4.delete_beg","5.delete_end")
ch=int(input())

if(ch==1):
    print("enter the data")
    data=input()
    l1.insert_begin(data)
    l1.printlist()
elif(ch==2):
    print("enter the data")
    data=input()
    l1.insert_end(data)
    l1.printlist()
elif(ch==3):
    print("enter the data&previous node data")
    data=input()
    pre=input()
    l1.insert_mid(data,pre)
    l1.printlist()
elif(ch==4):
    l1.del_beg()
    l1.printlist()
elif(ch==5):
    print("enter the data")
    data=input()
    l1.delete(data)
    l1.printlist()
else:
    print("none of these choice")
 






    
 
