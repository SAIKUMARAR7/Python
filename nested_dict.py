import json
import array
x='[{"name":"luke","id":1,"connect":{"phone":2222222,"mail":"abc@gmail.com","others":["facebook","linkedin"]}},{"name":"ric","id":2,"connect":{"phone":333333,"mail":"xyz@gmail.com","others":["facebook","linkedin"]}},{"name":"lucy","id":3,"connect":{"phone":555555,"mail":"dfg@gmail.com","others":["facebook","linkedin","skype"]}}]'
y=json.loads(x)
a=[y[0],y[1],y[2]]
#a[1]=y[1]
#a[2]=y[2]
fc="false"
lc="false"
sc="false"
name=input()
for i in range(0,3):
    if a[i]["name"]==name:
        print("id:",a[i]["id"])
        print("name:",a[i]["name"])
        print("phone:",a[i]['connect']['phone'])
        print("mail:",a[i]['connect']['mail'])
        s=(a[i]['connect']['others'])
    #for i in s:
    #print(i)
        if "facebook" in s:
            fc="true"
        if "linkedin" in s:
            lc="true"
        if "skype"in s:
            sc="true"
        print("facebook:"+fc)
        print("skype:"+sc)
        print("linkedin:"+lc)
    else:
        continue

