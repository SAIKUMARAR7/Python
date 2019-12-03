import json
f=open("c.json","r")
x=f.read()
print(x)
s=open("cd.json",'w')
c=json.dumps(x)
s.write(c)
