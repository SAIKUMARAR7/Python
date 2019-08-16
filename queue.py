from pythonds.basic import Queue

def simpleQ(name,num):
    s=Queue()
    for i in name:
        s.enqueue(i)
    while s.size()>1:
        for i in range(num):
            s.enqueue(s.dequeue())                                                                                                                                                                                                                                                                                             
        s.dequeue()
    return(s.dequeue())
            

print(simpleQ(["sai","nandy","nachi","joseph","nirmal","milton"],15))

