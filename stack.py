class stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def pop(self):
        if len(self.stack)<=0:
            print("stack is Empty")
        else:
           return self.stack.pop()
    def printlist(self):
        print(self.stack)
l1=stack()
l1.add("mon")
l1.add(22)
l1.add("d")
ch='y'
while ch=='y':
    a=input("enter input")
    l1.add(a)
    ch=input("y/n :")
    #print(l1.pop())
l1.printlist()
